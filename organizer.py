import os
import shutil
from pathlib import Path
MAPPING = {
    '.pdf': 'Documents',
    '.jpg': 'Images',
    '.png': 'Images',
    '.zip': 'Archives',
    '.py' : 'Code',
    '.csv' : 'Documents'
}

files_count = 0

for entry in os.scandir('.'):
    if entry.is_file():
        ext = Path(entry.name).suffix.lower()

        if ext in MAPPING:
            folder = MAPPING[ext]

            os.makedirs(folder, exist_ok=True)

            try:
                shutil.move(entry.name, f"{folder}/{entry.name}")
                files_count += 1
                print(f"Moved: {entry.name} -> {folder}")
            except Exception as e:
                print(f"Error moving {entry.name}: {e}")

print(f"\n{files_count}")