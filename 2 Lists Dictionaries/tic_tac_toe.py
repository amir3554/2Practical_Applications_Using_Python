game_dict = {
    '1':'01', '2':'02', '3':'03',
    '4':'04', '5':'05', '6':'06',
    '7':'07', '8':'08', '9':'09'}

def check_game_w():
        if (game_dict['1'] == game_dict['2'] and game_dict['1'] == game_dict['3'] and game_dict['2'] == game_dict['3']):
        #first line
            print('w')
            return False
        if game_dict['4'] == game_dict['5'] and game_dict['4'] == game_dict['6'] and game_dict['5'] == game_dict['6']:
        #second line
            print('w')
            return False
        if game_dict['7'] == game_dict['8'] and game_dict['7'] == game_dict['9'] and game_dict['8'] == game_dict['9']:
        #third line
            print('w')
            return False
        if game_dict['1'] == game_dict['5'] and game_dict['1'] == game_dict['9'] and game_dict['5'] == game_dict['9']:
        # tilte line 1 5 9
            print('w')
            return False
        if game_dict['3'] == game_dict['5'] and game_dict['3'] == game_dict['7'] and game_dict['5'] == game_dict['7']:
        # tilte line 3 5 7
            print('w')
            return False
        if game_dict['1'] == game_dict['4'] and game_dict['1'] == game_dict['7'] and game_dict['4'] == game_dict['7']:
        # first colomn
            print('w')
            return False
        if game_dict['2'] == game_dict['5'] and game_dict['2'] == game_dict['8'] and game_dict['5'] == game_dict['8']:
        # second colomn
            print('w')
            return False
        if game_dict['3'] == game_dict['6'] and game_dict['3'] == game_dict['9'] and game_dict['6'] == game_dict['9']:
        # third colomn
            print('w')
            return False
        return True


def game_printer():
        print(f'''
{game_dict["1"]}          |          {game_dict["2"]}         |        {game_dict["3"]}
-----------------+------------------+-----------------
{game_dict["4"]}          |          {game_dict["5"]}         |        {game_dict["6"]}
-----------------+------------------+-----------------
{game_dict["7"]}          |          {game_dict["8"]}         |        {game_dict["9"]}

        ''')



while True:

    check_game_w()
    game_printer()
    if not check_game_w():
        break 


    turn = input("X its your turn, inter an index ")
    turn = str(turn)
    if turn in game_dict:
        game_dict[turn] = 'X'

    check_game_w()
    game_printer()
    if not check_game_w():
        break 


    turn = input("O its your turn, inter an index ")
    turn = str(turn)
    if turn in game_dict:
        game_dict[turn] = 'O'
