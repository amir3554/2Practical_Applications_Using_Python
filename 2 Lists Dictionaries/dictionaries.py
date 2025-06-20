names = ['Amir', 'mariam', 'saeed', 'sara', 'mae', 'dee']

salary = [1000, 500, 2000, 800, 2000, 1500]

numbers = ['458802145', '124883216', '660431274', '967332304', '358935442', '76346255']

# Dictionaries 

Amir = {
    'name' : 'Amir',
    'salary' : 2000,
    'number' : '0599257557',
    'skills' : ['HTML', 'python', 'CSS']
    }
print(Amir['salary'])
print(Amir)
print(Amir['skills'][0])
print(Amir['number'])

print('----------------------------')

my_animals = ['cat', 'bird', 'mouse']
animals = ['bird', 'cat', 'mouse']

print(my_animals == animals)
print(animals[0])
print(my_animals[0])

print('----------------------------')

my_dict = {'name' : 'Meow', 'species' : 'cat', 'age' : 5}
dict2 = {'species' : 'cat', 'age' : 5, 'name' : 'Meow'}

print(my_dict == dict2)


print('----------------------------')

B_date = {}

user_name = input('inter your name')
user_birth_date = input('Inter your birthday')

print('----------------------------')

dictionary = {'Amir': 'apr9', 'mae': 'sep24', 'mariam':'may10'}

while True:
    print('Inter a name to know their birthday, (Pres enter to exit.) ')
    name = input()
    if  not name:
        break
    if name in dictionary:
        print(f'{dictionary[name]} is the birth day of {name}')
    if name not in dictionary:
        print("The name not in the dictionary, but what is their birth day to update our data base.")
        b_date = input()
        dictionary[name] = b_date

print('----------------------------')
print('----------------------------')
print('----------------------------')

Amir = {
    'name' : 'Amir',
    'salary' : 2000,
    'number' : '0599257557',
    'skills' : ['HTML', 'python', 'CSS']
    }
print(f'My Name is {Amir['name']}, and my hoppy is {Amir.get('hoppy', 'no info')}')

print('----------------------------')

# set default

print(Amir.setdefault("name", 'zoe'))
if 'language' not in Amir:
    Amir['language'] = 'CSS'

print('----------------------------')

# update

Amir.update({'salary' : 2500})
Amir.update({'pet' : 'cat'})

print('----------------------------')

#clear

#لافراغ القاموس من القيم الت فيه


