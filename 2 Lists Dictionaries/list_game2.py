list_names = ['amir', 'mariam', 'dawood', 'sara', 'saeed', 'reem', 'raool', 'sameer', 'hamed', 'jamie', 'osama', 'alaa']

print(list_names)
print('_______________________________________________')
Attempts = 12
print('have 12 Attempts')
print('_______________________________________________')
name = input('first of all , whats your name. ')
print(f"hello {name}, nice to meet you, okey let's start.")
print('_______________________________________________')


#while True:
user_guess_letter = input("You have a list of name you have to choose the name that i have chosen , now enter you user_guess_letter.")

if user_guess_letter.isdigit():
        print('please enter a name not a number.')
    #    continue

if not user_guess_letter:
        print("You have not enter a name.")
    #    continue
    
    #if user_guess_letter not in list_names:
    #    print('please enter a name from the list')
    #    continue

import random
'''
word ='amoor' # random.choice(list_names)  
    #for i in word:
    #    print('-\n')
dash_list = []
letters_list = []

for i in word:
    dash_list.append('-')
    letters_list.append(i)

print(dash_list)
while Attempts > 0:
    user_guess_letter = input(''You have a list of names,
you have to choose the name that i have chosen
now enter you user_guess_letter.'')
    if user_guess_letter in letters_list:
        dash_list[letters_list.index(user_guess_letter)] = user_guess_letter
        print(dash_list)
    else:
        Attempts -= 1
        print(f'Try again, You have {Attempts} left')

#    if user_guess_letter in word:
#        for i in range(len(word)):
#            dash_list.append('-')
#        print(dash_list)
            

#        for i in word:
#            letters_list.append(i)
#            if :
#                letters_list[i] = 
#                print(i)
#                continue

    if user_guess_letter not in word:
        Attempts -= 1
        print('You have guessed the wrong letter')
'''

word2 = random.choice(list_names)

guesess = ''

while Attempts > 0:

    failed = 0

    for char in word2:
        
        if char in guesess:
            print(char)

        else:
            print('-')
            failed += 1

    if failed == 0:
        print('You win')
        print(' the name is ' + word2)
        break

    user_guess_letter = input("You have a list of name you have to choose the name that i have chosen , now enter you user_guess_letter.")
    guesess += user_guess_letter

    if char not in word2:
        Attempts -= 1
        print("wrong gusee")
        print(f"You have {Attempts} left")

    if Attempts == 0:
        print('You lost')
        break
