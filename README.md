# File Organizer by Extension (Python)

A simple Python automation script that organizes files in a folder
by their file extensions.

Files are moved into subfolders such as `pdf`, `jpg`, `txt`, etc.
Files without extensions are placed in a `no_extension` folder.

## Features

- Organizes files by extension
- Handles files with no extension
- Prevents overwriting by auto-renaming duplicates
- Includes a `dry_run` mode to preview changes safely

## How to Run

1. Make sure Python 3 is installed
2. Clone or download this repository
3. Open `Organizing.py`
4. Set the folder you want to organize:

```python
TARGET_FOLDER = r"path/to/your/folder"
```
5.To actually move files, set dry_run=False
```python
organize_by_extension(TARGET_FOLDER, dry_run=False)
```
