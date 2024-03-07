

x_o = {0:" ", 1:" ", 2:" ", 10:" ", 11:" ", 12:" ", 20:" ", 21:" ", 22:" "}

def penman():
    print('  0 1 2')
    print(f'0 {x_o[0]} {x_o[1]} {x_o[2]}')
    print(f'1 {x_o[10]} {x_o[11]} {x_o[12]}')
    print(f'2 {x_o[20]} {x_o[21]} {x_o[22]}')
def checkinp(plinput, char):
    if plinput not in (0,1,2,10,11,12,20,21,22) or x_o[plinput] in ('x', 'o'):
        return False
    x_o[plinput] = char
    return True

def game_status():
    win = False

    win_coord = (
        (0,1,2), (10,11,12), (20,21,22), (0,10,20),
        (1,11,21), (2,12,22), (0,11,22), (2,11,20)
    )

    for pos in win_coord:
        if x_o[pos[0]] == 'x' and x_o[pos[1]] == 'x' and x_o[pos[2]] == 'x':
            win = 'x'
        elif x_o[pos[0]] == 'o' and x_o[pos[1]] == 'o' and x_o[pos[2]] == 'o':
            win = 'o'

    return win
def step4():

    step = 1

    player_x = 'x'
    player_o = 'o'
    cur_player = 1

    penman()
    while step<10 and game_status() == False:
        if step % 2 == 0:
            cur_player = player_o
        else:
            cur_player = player_x
        print('-------------------')
        plinput = input(f'Ход игрока {cur_player}. \nВведите координаты поля:')

        if (checkinp(int(plinput), cur_player)):
            print('-------------->>>')

            penman()
            step += 1
        else:
            print('Неправильный ход! Попробуйте снова!')
            penman()
    if step == 10 and game_status() == False:
        print('Увы. Ничья :(')
    else:
        print(f'Победил игрок {game_status()}!')

print("Начало игры!")
step4()