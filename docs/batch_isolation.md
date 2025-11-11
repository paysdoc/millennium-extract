# Batch Isolation in Parallel Downloads

## Problem

When running multiple parallel download processes, the web-based review system was not properly isolated, causing images and HTML files from different batches to overwrite each other.

## Root Cause

The `SimpleReviewGenerator` class used a **shared directory** for all batches:

```python
self.review_dir = Path("sourced_images/review")  # ❌ Shared!
```

Even though `batch_id` was used to namespace `localStorage` keys, the physical files were in the same directory:

```python
new_filename = f"{character.id}_{idx}.jpg"  # Only character ID
new_path = self.review_dir / new_filename    # Same dir for all batches
```

### Why This Caused Problems

1. **Process A** downloads characters 1-5 for category M (Musicians)
2. **Process B** downloads characters 1-5 for category P (Philosophers)
3. Both write to `sourced_images/review/`
4. If character IDs overlap, files overwrite each other
5. HTML pages reference wrong images
6. Selection data gets mixed between batches

## Solution

### Batch-Specific Directories

Changed to use **batch-specific subdirectories**:

```python
self.batch_id = batch_id or "default"
self.review_dir = Path("sourced_images/review") / self.batch_id  # ✅ Isolated!
```

Now each batch gets its own directory:
- `sourced_images/review/M_batch1/` - Musicians batch 1
- `sourced_images/review/P_batch1/` - Philosophers batch 1
- `sourced_images/review/M_batch2/` - Musicians batch 2

### Directory Structure

```
sourced_images/
└── review/
    ├── M_batch1/           # Category M, batch 1
    │   ├── index.html
    │   ├── submit.html
    │   ├── 1_review.html   # Character ID 1 review page
    │   ├── 1_1.jpg         # Character ID 1, image 1
    │   ├── 1_2.jpg         # Character ID 1, image 2
    │   └── ...
    ├── P_batch1/           # Category P, batch 1
    │   ├── index.html
    │   ├── submit.html
    │   ├── 1_review.html   # Different character ID 1
    │   └── ...
    └── default/            # Default batch (if no batch_id specified)
        └── ...
```

### HTTP Server Configuration

The HTTP server serves from the **root review directory**:

```python
review_dir_root = Path("sourced_images/review")
pid = start_http_server(port, review_dir_root)
```

URLs include the batch ID path:
```
http://localhost:8000/M_batch1/index.html
http://localhost:8001/P_batch1/index.html
```

## Isolation Guarantees

### ✅ Fully Isolated
- **HTML files** - Each batch has its own index.html, submit.html, review pages
- **Image files** - Each batch has its own copies of candidate images
- **localStorage** - Keys are namespaced with `batch_id` prefix
- **HTTP ports** - Each process gets a unique port (8000-8020 range)

### ⚠️ Shared Resources
- **temp_candidates/** - Temporary downloads are shared
  - Safe because filenames include character ID and name
  - Can use more disk space during parallel downloads
  - Clean up with: `python3 -m src.download_images.cleanup_temp`

- **wikimedia/by_character_id/** - Final downloaded images
  - This is intentional - we want to share validated downloads
  - Protected by character ID uniqueness

## Testing

Run the isolation test:

```bash
python3 test_batch_isolation.py
```

Expected output:
```
✅ All isolation tests passed!
✅ Batch 1 uses: sourced_images/review/TEST_BATCH_1
✅ Batch 2 uses: sourced_images/review/TEST_BATCH_2
✅ Directories are isolated
```

## Running Parallel Downloads

### Safe Parallel Execution

You can now safely run multiple downloads in parallel:

```bash
# Terminal 1 - Musicians
python3 -m src.download_images.web_main M 5 0

# Terminal 2 - Philosophers
python3 -m src.download_images.web_main P 5 0

# Terminal 3 - Artists
python3 -m src.download_images.web_main A 5 0
```

Each will:
1. Get a unique port (8000, 8001, 8002)
2. Use a unique batch directory (M_batch1, P_batch1, A_batch1)
3. Have isolated HTML pages and images
4. Have isolated localStorage selections

### View Active Batches

```bash
python3 -m src.download_images.cleanup_servers list
```

Output:
```
Active HTTP Servers
================================================================================
Port 8000:
  Category: M
  Batch: Batch 1 (chars 1-5)
  URL: http://localhost:8000/M_batch1/index.html

Port 8001:
  Category: P
  Batch: Batch 1 (chars 1-5)
  URL: http://localhost:8001/P_batch1/index.html
```

### Cleanup

Stop all servers:
```bash
python3 -m src.download_images.cleanup_servers stop-all
```

Clean up temp files:
```bash
python3 -m src.download_images.cleanup_temp
```

## Migration Notes

### Old Batches

If you have old review pages in `sourced_images/review/` (not in subdirectories):
- These are from the old non-isolated system
- They can be safely deleted or moved
- New batches will always use subdirectories

### Manual Cleanup

Remove old review files:
```bash
rm -rf sourced_images/review/*.html
rm -rf sourced_images/review/*.jpg
```

Batch directories will remain:
```bash
ls sourced_images/review/
# M_batch1/  P_batch1/  A_batch1/  etc.
```
