import os
import re
from pathlib import Path

def flip_date_format(name: str) -> str:
    """
    تعديل تنسيق التاريخ في الاسم من 'DD-MM-YYYY' إلى 'YYYY-MM-DD'.
    """
    match = re.search(r'(\d{2})-(\d{2})-(\d{4})', name)
    if match:
        return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"
    raise ValueError("No valid date format found in the name.")

def check_file_name(file_name: str) -> bool:
    """
    التحقق من أن اسم الملف يحتوي على تاريخ بالتنسيق 'DD-MM-YYYY'.
    """
    return bool(re.search(r'\d{2}-\d{2}-\d{4}', file_name))

# تحديد مسار المجلد
folder_path = Path.home() / 'Desktop' / 'Python_2024_2025' / 'newfolder'

# التأكد من أن المسار مجلد صالح
if not folder_path.is_dir():
    raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

# قراءة الملفات من المجلد
for file in folder_path.iterdir():
    if not file.is_file():
        continue

    file_name = file.name
    if not check_file_name(file_name):
        continue

    try:
        new_name = flip_date_format(file_name)
        new_path = file.with_name(new_name)
        os.rename(file, new_path)
        print(f"Renamed: {file_name} -> {new_name}")
    except ValueError as e:
        print(f"Skipped '{file_name}': {e}")
