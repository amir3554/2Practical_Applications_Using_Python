import openpyxl, sys
from pathlib import Path

# when the user inters 5 , this will appear in the multitable.xlsx :
# 1   2   3   4   5
# 2   4   6   8  10
# 3   6   9  12  15
# 4   8   12 16  20
# 5  10   15 20  25

def trash1():# just for tests , dont look in it
    user_input = int(input())
    for i in range (1, user_input +1):
        print(i, end='')
        for j in range(1, i +1):
            print(j, end=' ')
            #print(i + j)
    #def the_table_numbers():
    user_input = int(input())
    resault1 = []
    for i in range (1, user_input +1):
        for j in range(1, user_input +1):
            resault1.append(i * j)
    #    return resault1
    letters = ["A", "B", "C", "D", "E", "F"] 
    for i2 in range(1, user_input +1):
        for j2 in range(1, user_input +1):
                sheet[f"{letters[i2]}{str(j2)}"] = f'{resault1[j2 -1]}'
                #resault1.pop(j2)
                sheet[f"{letters[j2]}{str(i2)}"] = f'{resault1[j2 -1]}'  

if len(sys.argv) == 2:

    try:
        number = int(sys.argv[1])
    
    except Exception as e:
        print('Bruh')


    file = openpyxl.Workbook()
    sheet = file.active
   
    for col in range(1, number +1):
        for cycle in range(1, number +1):
            
            sheet.cell(row= cycle, column= col).value = f"{col * cycle}"
        
    file.save(filename=Path.home()/ Path("Desktop", "tests")/ f'multitable{number}.xlsx')

    print(f'The file was saved at: {Path.home()}{file.path}')

else:
    print("Please inter the file name , then the number you whant a multiplayer table for it.")

