#join 

list1 = ['hello', 'world']
print(' '.join(list1))
print('-'.join(list1))
print(type(' abc '.join(list1)))



print("--------------------------------------")
#split
#عكس التابع جوين حيث يأخذ ساسلة نصة و يعيد قائمة `~`

str1 = "Amoor Meow Love Meow Cats"
print(str1.split(' '))

str2 = 'MyABCnameABCisABCAmoor'
print(str2.split('ABC'))

str3 = """Hello
How are you?
I'm fine thanks...
"""
print(str3.split('\n'))
print(str3.splitlines())




