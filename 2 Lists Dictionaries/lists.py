employees = ['hasan', 'saeed', 'reem', 'dana', 'sameer', 'rwan', 'mahmood']

print(employees)
print(employees[0])
print(employees[1])
print(employees[5])
print(employees[-1])
print(employees[-2])
#print(employees[50])


print(employees[1:3])
print(employees[2:])
print(employees[:3])
print(employees[:])
print(employees[1:3:2])
print(employees[1:5:1])

employees[4] = 'sara'
employees[0:2] = 'Amir', 'salwa'

print("---------------------------------------------")
# for loops

for i in range(len(employees)):
    print(employees[i])

for i in range(len(employees)):
    print(f'Index : {i + 1}, Name : {employees[i]}')


print("---------------------------------------------")
#enumerate

for index, item in enumerate(employees):
    print(f"index is {index}, name is {item}")


print("---------------------------------------------")
# in and not in

print('sara' in employees)


print("---------------------------------------------")
#test

the_input = str(input("inter the employee name."))

if the_input in employees:
    print(f'Its {True}, the {the_input} is an employee with the number {employees.index(the_input) + 1}')
else:
    print(f'The {the_input}, is not found.')

print("---------------------------------------------")
# random.chose()  random.shuffle()
import random

print(random.choice(employees))
#print(random.shuffle(employees))




