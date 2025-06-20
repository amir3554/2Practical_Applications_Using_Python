import csv
from pathlib import Path

file = open(Path.home() / Path("Desktop", "tests", "employees_1.csv"))
reder = csv.reader(file)

data = list(reder)
print(data)
print(data[0][1])
print(data[1][0])
print(data[3][2])
print(data[1][1])

for row in data:
    print(f'Row #{reder.line_num} {str(row)}.')

file = open(Path.home() / Path("Desktop", "tests", "employees_1.csv"), 'a', newline='')

header = ["name", "salary", "date"]

data = [
    ["amoor", 1000, "2024/9/4"],
    ["mariam", 900, "2021/5/3"],
    ["dawood", 1500, "2023/10/2"]
]

writer = csv.writer(file)
writer.writerow(header)
writer.writerows(data)
file.close()

# ctrl forword slash ("/")

# delimeter and lineterminator Keyword


#file = open(Path.home() / Path("Desktop", "tests", "employees_1.csv"), 'a', newline='')

#writer1 = csv.writer(file, delimiter='\t', lineterminator='\n-------------------\n')
#writer1.writerow([])
#writer1.writerow([])
#writer1.writerow([])
#file.close()
