import openpyxl
from pathlib import Path

file = openpyxl.load_workbook(Path.home() / Path('Desktop', 'tests', 'employees.xlsx'))

sheet1 = file['Sheet1']

sheet1['B7'] = "=SUM(B1:B6)"
sheet1['B8'] = "=average(B1:B6)"
sheet1['B9'] = '=COUNTIF(B1:B6, ">700")'

file.save(filename=Path.home() / Path('Desktop', 'tests', 'employees.xlsx'))
