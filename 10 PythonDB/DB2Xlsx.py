import openpyxl
import sqlite3
from pathlib import Path

Connection = sqlite3.connect(Path.home()/ Path("Desktop", "tests", "PythonDataBase.db"))
the_cursor = Connection.cursor()


EmployeesSelector = the_cursor.execute("SELECT * FROM employees").fetchall()


file = openpyxl.Workbook()
sheet =file.active

for row_num,row in enumerate(EmployeesSelector):
    for col_num,col_the_data in enumerate(row):
        sheet.cell(row=row_num+1, column=col_num+1).value = col_the_data

file.save(Path.home() / Path("Desktop", "tests", "DBToExcil.xlsx"))
file.close()
Connection.close()
