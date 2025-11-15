"""
File operations for downloading and saving images.
Single Responsibility: Handle all file I/O operations.
"""
import json
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple
from .models import ImageInfo, DownloadMetadata
from .config import WikimediaConfig, DownloadConfig


class FileManager:
    """
    Manages file operations for image downloads and metadata.
    """

    def __init__(self, config: DownloadConfig = None, similarity_threshold: int = 20):
        """
        Initialize file manager.

        Args:
            config: Download configuration (uses default if None)
            similarity_threshold: Deprecated parameter, kept for backwards compatibility
        """
        self.config = config or DownloadConfig()

        # Image format magic bytes
        self.IMAGE_SIGNATURES = {
            b'\xFF\xD8\xFF': 'jpg',  # JPEG
            b'\x89PNG\r\n\x1a\n': 'png',  # PNG
        }

        # Corrupted file signature to reject
        self.CORRUPTED_SIGNATURE = b'\x41\x54'  # 0x41 0x54

    def validate_image_data(self, data: bytes) -> Tuple[bool, Optional[str]]:
        """
        Validate that downloaded data is a valid image format.

        Args:
            data: Raw image data bytes

        Returns:
            Tuple of (is_valid, file_extension)
            - is_valid: True if data is a valid image, False otherwise
            - file_extension: 'jpg' or 'png' if valid, None otherwise
        """
        if len(data) < 8:
            return False, None

        # Check for corrupted signature (0x41 0x54)
        if data[:2] == self.CORRUPTED_SIGNATURE:
            return False, None

        # Check for valid image signatures
        for signature, extension in self.IMAGE_SIGNATURES.items():
            if data[:len(signature)] == signature:
                return True, extension

        return False, None

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

    def download_image(self, url: str, filepath: Path) -> Tuple[bool, Optional[str]]:
        """
        Download image from URL to file with validation.

        Args:
            url: Image URL
            filepath: Destination file path

        Returns:
            Tuple of (success, actual_extension)
            - success: True if download and validation successful
            - actual_extension: The actual image format ('jpg' or 'png'), or None if failed
        """
        try:
            response = requests.get(
                url,
                headers=WikimediaConfig.HEADERS,
                timeout=WikimediaConfig.DOWNLOAD_TIMEOUT_SECONDS,
                stream=True
            )
            response.raise_for_status()

            # Download to memory first to validate
            data = b''
            for chunk in response.iter_content(chunk_size=self.config.CHUNK_SIZE):
                data += chunk

            # Validate image format
            is_valid, actual_extension = self.validate_image_data(data)
            if not is_valid:
                print(f"    ❌ Invalid image format (corrupted or unsupported)")
                return False, None

            # Create parent directories if needed
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Adjust filepath extension if needed
            if actual_extension and filepath.suffix.lower() != f'.{actual_extension}':
                filepath = filepath.with_suffix(f'.{actual_extension}')

            # Write validated data to file
            with open(filepath, 'wb') as f:
                f.write(data)

            return True, actual_extension

        except Exception as e:
            print(f"    ❌ Download failed: {e}")
            return False, None

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
        # Generate initial filename with default extension
        filename = self.generate_filename(
            character.id,
            character.type or "?",
            character.name or "Unknown",
            rank,
            extension="jpg"  # Default, will be updated based on actual format
        )

        image_path = output_dir / filename

        # Download image with validation
        success, actual_extension = self.download_image(image_info.url, image_path)
        if not success:
            return False

        # Update paths with actual extension if different
        if actual_extension and actual_extension != 'jpg':
            new_filename = self.generate_filename(
                character.id,
                character.type or "?",
                character.name or "Unknown",
                rank,
                extension=actual_extension
            )
            image_path = output_dir / new_filename

        metadata_path = image_path.with_suffix('.json')

        print(f"    ✅ Downloaded ({actual_extension.upper()})")

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
