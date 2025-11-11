"""
File operations for downloading and saving images.
Single Responsibility: Handle all file I/O operations.
"""
import json
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional
from .models import ImageInfo, DownloadMetadata
from .config import WikimediaConfig, DownloadConfig
from .image_similarity import ImageValidator


class FileManager:
    """
    Manages file operations for image downloads and metadata.
    """

    def __init__(self, config: DownloadConfig = None, similarity_threshold: int = 20):
        """
        Initialize file manager.

        Args:
            config: Download configuration (uses default if None)
            similarity_threshold: Image similarity threshold (0-64, lower = more similar required)
        """
        self.config = config or DownloadConfig()
        self.validator = ImageValidator(similarity_threshold)

    def generate_filename(
        self,
        character_id: int,
        category: str,
        name: str,
        rank: int,
        extension: str = "jpg"
    ) -> str:
        """
        Generate standardized filename for image.

        Args:
            character_id: Character ID (integer)
            category: Character category/type
            name: Character name
            rank: Image rank (1 for primary, 2+ for alternatives)
            extension: File extension

        Returns:
            Filename string
        """
        # Normalize name for filesystem
        normalized_name = name.replace(' ', '_').replace('/', '_')

        if rank == 1:
            return f"{character_id}_{category}_{normalized_name}.{extension}"
        else:
            return f"{character_id}_{category}_{normalized_name}_alt{rank-1}.{extension}"

    def download_image(self, url: str, filepath: Path) -> bool:
        """
        Download image from URL to file.

        Args:
            url: Image URL
            filepath: Destination file path

        Returns:
            True if successful, False otherwise
        """
        try:
            response = requests.get(
                url,
                headers=WikimediaConfig.HEADERS,
                timeout=WikimediaConfig.DOWNLOAD_TIMEOUT_SECONDS,
                stream=True
            )
            response.raise_for_status()

            # Create parent directories if needed
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Write file in chunks
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=self.config.CHUNK_SIZE):
                    f.write(chunk)

            return True

        except Exception as e:
            print(f"    ❌ Download failed: {e}")
            return False

    def save_metadata(self, metadata: DownloadMetadata, filepath: Path) -> bool:
        """
        Save metadata to JSON file.

        Args:
            metadata: Metadata object
            filepath: Destination file path (should be .json)

        Returns:
            True if successful, False otherwise
        """
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)

            with open(filepath, 'w') as f:
                json.dump(metadata.to_dict(), f, indent=2)

            return True

        except Exception as e:
            print(f"    ❌ Failed to save metadata: {e}")
            return False

    def create_metadata(
        self,
        character,
        image_info: ImageInfo,
        rank: int
    ) -> DownloadMetadata:
        """
        Create metadata object from character and image info.

        Args:
            character: Character object
            image_info: ImageInfo object
            rank: Image rank (1 for primary, 2+ for alternatives)

        Returns:
            DownloadMetadata object
        """
        return DownloadMetadata(
            character_name=character.name or "",
            character_id=character.id,
            category=character.type or "?",
            first_names=character.first_names,
            biography=character.biography,
            birth_date=character.birth_date,
            death_date=character.death_date,
            wikimedia_title=image_info.title,
            wikimedia_url=image_info.url,
            width=image_info.width,
            height=image_info.height,
            aspect_ratio=image_info.aspect_ratio,
            score=image_info.score,
            download_timestamp=datetime.now().isoformat(),
            rank=rank
        )

    def download_with_metadata(
        self,
        character,
        image_info: ImageInfo,
        output_dir: Path,
        rank: int
    ) -> bool:
        """
        Download image and save metadata together.

        Args:
            character: Character object
            image_info: ImageInfo object
            output_dir: Output directory
            rank: Image rank

        Returns:
            True if both operations successful
        """
        # Generate filenames
        filename = self.generate_filename(
            character.id,
            character.type or "?",
            character.name or "Unknown",
            rank
        )

        image_path = output_dir / filename
        metadata_path = image_path.with_suffix('.json')

        # Download image
        if not self.download_image(image_info.url, image_path):
            return False

        print(f"    ✅ Downloaded")

        # Validate image similarity against cache
        should_keep, reason = self.validator.should_keep_image(
            image_path,
            character.name or "Unknown",
            character.id,
            character.type or "?"
        )

        if not should_keep:
            print(f"    ❌ Rejected: {reason}")
            # Delete the downloaded image
            try:
                image_path.unlink()
            except Exception as e:
                print(f"    ⚠️  Could not delete rejected image: {e}")
            return False

        print(f"    ✅ Validated: {reason}")

        # Save metadata
        metadata = self.create_metadata(character, image_info, rank)
        self.save_metadata(metadata, metadata_path)

        return True

    def ensure_output_dir(self, output_dir: Optional[Path] = None) -> Path:
        """
        Ensure output directory exists.

        Args:
            output_dir: Directory path (uses default if None)

        Returns:
            Path object for output directory
        """
        if output_dir is None:
            output_dir = Path(self.config.OUTPUT_DIR)

        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir
