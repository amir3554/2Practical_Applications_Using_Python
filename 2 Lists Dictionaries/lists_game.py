list_names = ['amir', 'mariam', 'salwa', 'sara', 'saeed', 'reem', 'dana', 'sameer', 'rwan', 'shams', 'osama', 'alaa']
print(list_names)
print('_______________________________________________')
Attempts = 12
print('have 12 Attempts')
print('_______________________________________________')
name = input('first of all , whats your name. ')
print(f"hello {name}, nice to meet you, okey let's start.")
print('_______________________________________________')


while True:
    guess = input("You have a list of name you have to choose the name that i have chosen , now enter you guess.")

    if guess.isdigit():
        print('please enter a name not a number.')
        continue

    if not guess:
        print("You have not enter a name.")
        continue
    
    if guess not in list_names:
        print('please enter a name from the list')
        continue

    import random
    the_com =random.choice(list_names) #'amoor' 

    if guess != the_com:
        Attempts -= 1
        print(f"You are wrong , I choosed '___{the_com}___', now you have _{Attempts}_ Attempts left.")
        if Attempts == 0:
            print('You lost, you have no Attemts left')
            break
        continue

    if guess in list_names:
        print('You win !!!')
        break













