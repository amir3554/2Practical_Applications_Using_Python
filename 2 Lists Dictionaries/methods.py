# list_name.appened(the_new_value)  list_name.insert(index, the_new_value)

employees = ['amir','salwa','sara','hasan', 'saeed', 'reem', 'dana', 'sameer', 'rwan']

employees.append('shams')

employees.insert(1, 'mariam')
print(employees)

old_employees = ['osama', 'alaa']

employees.append(old_employees)
print(employees)
print(employees[-1])
print(employees[-1][1])

print("------------------------------------------")
#extend remove
employees.remove(old_employees)
employees.extend(old_employees)

print(employees)

print("------------------------------------------")
# del statement

del employees[4]

print("------------------------------------------")
# sort

numbers = [1, 3, 8, 5, 7, -7, 9, 11, 32]

print(numbers.sort())
print(numbers.sort(reverse=True))

employees_list2 = [employees]
print(employees_list2)

print(employees_list2.sort())

spam = [1,2,3,4,'alice','sam']
#spam.sort()


print("------------------------------------------")
#reverse

