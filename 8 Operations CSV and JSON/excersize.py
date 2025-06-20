import csv, os
from pathlib import Path


Folder_list = os.listdir(Path.home() / Path("Desktop", "tests"))
csv_files = []
for file in Folder_list:
    if file.endswith("csv"):
        csv_files.append(file)


for each in csv_files:
    the_file = open(Path.home() / Path("Desktop", "tests", f"{each}"))
    The_reader = csv.DictReader(the_file)
    
    the_new_file = open(Path.home() / Path("Desktop", "tests", f"Up_date_{each}"), 'w', newline='')
    The_writer = csv.DictWriter(the_new_file, ["Name", "Salary", "Date"])
    
    for row in The_reader:
        if row["Name"] == "Name": 
            continue
        else:
            The_writer.writerow(row)
