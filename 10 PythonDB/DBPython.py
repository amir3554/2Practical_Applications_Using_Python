import sqlite3
from pathlib import Path


SqlConnection = sqlite3.connect(Path.home() / Path("Desktop", "tests", "PythonDataBase.db"))
the_cursor = SqlConnection.cursor()

command1 = """CREATE TABLE if not exists students(
FirstName VARCHAR(20),
LastName VARCHAR(20),
Age INTEGER)"""

the_cursor.execute(command1)

the_cursor.execute("INSERT INTO students VALUES ('Amoor', 'math', 18);")
the_cursor.execute("INSERT INTO students VALUES ('Mariam', 'phy', 18);")
the_cursor.execute("INSERT INTO students VALUES ('Saeed', 'cha', 19);")




SqlConnection.commit()
the_cursor.close()












