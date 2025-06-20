import csv
from pathlib import Path

file = open(Path.home()/ Path("Desktop", "tests", "employees_1.csv"))

Dict_Reader = csv.DictReader(file)

for row in Dict_Reader:
    print(f"{row["Name"]}, {row["Date"]}, {row["Salary"]}")
    
file.close()


file = open(Path.home()/ Path("Desktop", "tests", "employees_1.csv"), 'a', newline='')
Dict_Writer = csv.DictWriter(file, ["Name", "Salary", "Date"])
Dict_Writer.writerow({"Name":"Sali", "Salary":"1200", "Date":"2023/6/29"})
file.close()

