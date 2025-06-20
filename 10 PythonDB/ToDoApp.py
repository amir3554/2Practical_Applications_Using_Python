import sys
import sqlite3
from pathlib import Path

massage ="""'"a" => Add New Task  ')
'"d" => Delete a Task ')
'"s" => Show All Tasks')
'"u" => Update a Task ')
'"-s" => Save Data    ')
'"q" => Quit The App  ') : """

possible_input = ['a', 'd', 's', 'u', 'q', '-s']

def add_new_one(id = None, title = None, the_info = None, date = None, done = "False"):
    while True:
        try:
            print('Please add the (id, title, the_info and date) of the Task,after that done(optional), inter "-q" to exit.')
            print("Please ADD ** 'SPACE' '-' 'SPACE' ** betsween each.")
            user_input_info = input()
            if user_input_info == '-q':
                break
            id, title, the_info, date = user_input_info.split(' - ')

            if id and title and the_info and date:
                checked = input("Done is now Falese, if you whant to make it True inter y or press enter. ")
                if checked == 'y':
                    done = 'True'
                else:
                    done = "False"

                crsr.execute("INSERT INTO Tasks (id, title, the_info, date, done) VALUES (?, ?, ?, ?, ?);",(
                                         id, title, the_info, date, done))
                print(f"Your tasks has been added. ==>{id, title, the_info, date, done}")
            
            

            else:
                print("OOPSYY , There was an error , please try again and check your inputs and spaces")

        except Exception as e:
            print(f"There is an ERROR with your inputs, please try again\n{e}")
            continue


def delete_one(id = None):
    print("Please inter the id of the task you whant to delete.")
    id =input()
    if id:
        crsr.execute(f"DELETE FROM Tasks WHERE id = {id};")
        print(f"The task, whith an id:{id} has been deleted")

    elif not id:
        print('Please inter an id')

    elif id not in (crsr.execute(f"SELECT * FROM Tasks WHERE id = {id};")).fetchall():
        print("There is no task with this id")
    else:
        print("You have to enter an id for the row that you what to delete.")


def show_all_one():
    if crsr.execute("SELECT * FROM Tasks;").fetchall():
        for task in (crsr.execute("SELECT * FROM Tasks;").fetchall()):
            print(f"{task}")
    else:
        print("You have no tasks.")
    

def update_one(id = None, what_to_update = None, new_value = None):
    while True:
        try:
            print("Enter id, what to update (the colomn(id, title, the_info, date, done)) and new value, at the same order,  inter '-q' to exit.")
            print("Please ADD ** 'SPACE' '-' 'SPACE' ** betsween each.")
            user_input_info = input()
            if user_input_info == '-q':
                break
            id, what_to_update, new_value = user_input_info.split(' - ')

            if id and what_to_update and new_value:
                crsr.execute(f"UPDATE Tasks SET {what_to_update} = ? WHERE id = ?;", (new_value, id))
                print(f"The Tasks has been updated.")
            else:
                print("These is an error please check you inputs for the update.")
        except Exception as e:
            print(f"OPSYY... there is an ERROR with updating please check all inputs.\n{e}")


while len(sys.argv) == 2:# argv[0]= this file name, argv[1]= the data base name, argv[2]= Opration     #sql_DataBase_and_Oprations(file_name_input)
    try:
        Data_Base_name =  str(sys.argv[1]) + '.db'
        connection = sqlite3.Connection(Path.home() / Path("Desktop", "tests", f"{Data_Base_name}"))
        crsr = connection.cursor()
        crsr.execute("""CREATE TABLE if not exists Tasks(
                        id INTEGER,
                        title VARCHAR(20),
                        the_info TEXT,
                        date TEXT,
                        done VARCHAR);""")

        the_main_input = input(massage+'\n').strip().lower()

        if the_main_input not in possible_input:
            print("Please inter a valid input.\n")
            continue

        if the_main_input == 'a':
            add_new_one()

        if the_main_input == 'd':
            delete_one()

        if the_main_input == 's':
            show_all_one()

        if the_main_input == 'u':
            update_one()

        if the_main_input == '-s':
            print(f"Your Tasks has been saved.\n The DB file is {Data_Base_name}, in {Path.home() / Path("Desktop", "tests")}")
        connection.commit()

        if the_main_input == 'q':
            sys.exit()
            break

    except (Exception) as e:
        print(f"THIS IS AN EXCEPTION.\n{e}")
        continue
