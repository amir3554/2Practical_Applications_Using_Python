import shutil, os, re
from pathlib import Path

date_pattern = r'^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((20|19)\d\d)(.*?)$'
folder_path = Path.home() / Path('Desktop', 'newfolder')

for file_name in os.listdir(folder_path):
    search = re.search(date_pattern, file_name)

    if search == None:
        continue

    start_text_part = search.group(1)
    day_part = search.group(4)
    month_part = search.group(2)
    year_part = search.group(6)
    end_text_part = search.group(8)

    new_file_name = f'{start_text_part}{year_part}-{month_part}-{day_part}{end_text_part}'

    print(f"Renaming {file_name} To --> {new_file_name}")

    old_name = Path.home() / Path('Desktop', 'newfolder') / file_name
    new_name = Path.home() / Path('Desktop', 'newfolder') / new_file_name
    shutil.move(old_name, new_name)






