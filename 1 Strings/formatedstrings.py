name = 'Amir'

age = 18

print("Hello, my name " + name +  '. I am ' + str(age) + 'years old.')
print("Hello my name is %s , and my age is %d years old." % (name , age))

rank = 9.0

print("Hello my name is %s , and my age is %d years old, my rank is %.2f" % (name , age, rank))

print('-------------------------------------  %  ----------------------------')





print('-------------------------------  str.format  -------------------------')

print("Hello my name is {} , and my age is {} years old." .format(name , age))
print("Hello my name is {:s} , and my age is {:d} years old, my rank is {:.3f}".format(name , age, rank))
print("Hello my name is {1} , and my age is {0} years old." .format(age,name))
print("Hello my name is {name} , and my age is {name} years old." .format(name_ey = name, age_key = age))


print('-------------------------------  f strings  --------------------------')

print(f"Hello my name is {name} , and my age is {age} years old.")
print(f"Hello my name is {name} , and my age will be {age +1} years old.")



