def get_print(number_l: int, number_r: int, player_id: int):
    file_name_l = f'{number_l}.txt'
    file_name_r = f'{number_r}.txt'

    file_l = open(file_name_l)
    file_r = open(file_name_r)

    lines_l = file_l.read().splitlines()
    lines_r = file_r.read().splitlines()

    file_l.close()
    file_r.close()
    lines = []
    for i in range(len(lines_r)):
        lines.append(lines_l[i] + ' ' + lines_r[i][::-1].replace('\\', 'temp').replace('/', '\\').replace('temp', '/'))
    if player_id == 1:
        temp = lines[::-1]
        lines = []
        for line in temp:
            lines.append(line.replace('\\', 'temp').replace('/', '\\').replace('temp', '/'))
    return lines


def is_valid(move, l_player, r_player, l_opponent, r_opponent):
    if move == 'll':
        if l_player == 0:
            print('You cannot attack with an empty hand.')
            return False
        elif l_opponent == 0:
            print('You cannot attack an empty hand.')
            return False
        else:
            return True
    elif move == 'lr':
        if l_player == 0:
            print('You cannot attack with an empty hand.')
            return False
        elif r_opponent == 0:
            print('You cannot attack an empty hand.')
            return False
        else:
            return True
    elif move == 'rl':
        if r_player == 0:
            print('You cannot attack with an empty hand.')
            return False
        elif l_opponent == 0:
            print('You cannot attack an empty hand.')
            return False
        else:
            return True
    elif move == 'rr':
        if r_player == 0:
            print('You cannot attack with an empty hand.')
            return False
        elif r_opponent == 0:
            print('You cannot attack an empty hand.')
            return False
        else:
            return True
    elif move == 'div':
        if (l_player == 0) & (r_player % 2 == 0) or ((l_player % 2 == 0) & (r_player == 0)):
            return True
        else:
            print('To use div, you must have one empty hand and an even number on the other. Try again.')
            return False
    else:
        print(f'{move} is not a valid move.')
        return False


def move_p1(move, lp1, rp1, lp2, rp2):
    if move == 'll':
        lp2 = (lp2 + lp1) % 5
    elif move == 'lr':
        rp2 = (rp2 + lp1) % 5
    elif move == 'rl':
        lp2 = (lp2 + rp1) % 5
    elif move == 'rr':
        rp2 = (rp2 + rp1) % 5
    else:
        new_value = max(lp1, rp1) // 2
        lp1, rp1 = new_value, new_value
    return lp1, rp1, lp2, rp2


def move_p2(move, lp1, rp1, lp2, rp2):
    lp2, rp2, lp1, rp1 = move_p1(move, lp2, rp2, lp1, rp1)
    return lp1, rp1, lp2, rp2


def move_p(move, lp1, rp1, lp2, rp2, p):
    if p == 0:
        if is_valid(move, lp1, rp1, lp2, rp2):
            lp1, rp1, lp2, rp2 = move_p1(move, lp1, rp1, lp2, rp2)
            p = (p + 1) % 2
    else:
        if is_valid(move, lp2, rp2, lp1, rp1):
            lp1, rp1, lp2, rp2 = move_p2(move, lp1, rp1, lp2, rp2)
            p = (p + 1) % 2
    return lp1, rp1, lp2, rp2, p


if __name__ == '__main__':
    left_p1, right_p1, left_p2, right_p2 = 1, 1, 1, 1
    player = 0
    while ((left_p1 != 0) or (right_p1 != 0)) and ((left_p2 != 0) or (right_p2 != 0)):
        print('Current hands:')
        print('                 Player 2')
        print(f'       r ({right_p2})                    l ({left_p2})')
        p2_hands = get_print(right_p2, left_p2, 1)
        for line in p2_hands:
            print(line)
        print("------------------------------------------------")
        p1_hands = get_print(left_p1, right_p1, 0)
        for line in p1_hands:
            print(line)
        print(f'       l ({left_p1})                    r ({right_p1})')
        print('                 Player 1')
        m = input(f'Hi player {player + 1}! What is your move? (ll/lr/rl/rr/div)')
        left_p1, right_p1, left_p2, right_p2, player = move_p(m, left_p1, right_p1, left_p2, right_p2, player)
    print(f'Player {(player+1) % 2 + 1} wins!')

