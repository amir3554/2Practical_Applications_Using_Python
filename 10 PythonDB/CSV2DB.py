import sqlite3
import csv
from pathlib import Path


SqlConnection = sqlite3.connect(Path.home() / Path("Desktop", "tests", "PythonDataBase.db"))
the_cursor = SqlConnection.cursor()


the_cursor.execute("CREATE TABLE if not exists employees(Name VARCHAR(20),Salary INTEGER,Date VARCHAR(8))")


file_csv = open(Path.home() / Path("Desktop", "tests", "Up_date_employees_1.csv"), 'r')
the_data =csv.reader(file_csv)


for d in the_data:  
    the_cursor.execute(f"INSERT INTO employees VALUES ('{d[0]}',{d[1]},'{d[2]}')")
    print(d)


SqlConnection.commit()
the_cursor.close()



