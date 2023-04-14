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
        move_p = input(f'Hi player {player + 1}! What is your move? (ll/lr/rl/rr/div)')
        if move_p == 'll':
            if player == 0:
                if left_p2 == 0:
                    print('You cannot attack an empty hand.')
                elif left_p1 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    left_p2 = (left_p2 + left_p1) % 5
                    player = (player + 1) % 2
            else:
                if left_p1 == 0:
                    print('You cannot attack an empty hand.')
                elif left_p2 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    left_p1 = (left_p1 + left_p2) % 5
                    player = (player + 1) % 2
        elif move_p == 'lr':
            if player == 0:
                if right_p2 == 0:
                    print('You cannot attack an empty hand.')
                elif left_p1 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    right_p2 = (right_p2 + left_p1) % 5
                    player = (player + 1) % 2
            else:
                if right_p1 == 0:
                    print('You cannot attack an empty hand.')
                elif left_p2 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    right_p1 = (right_p1 + left_p2) % 5
                    player = (player + 1) % 2
        elif move_p == 'rl':
            if player == 0:
                if left_p2 == 0:
                    print('You cannot attack an empty hand.')
                elif right_p1 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    left_p2 = (left_p2 + right_p1) % 5
                    player = (player + 1) % 2
            else:
                if left_p1 == 0:
                    print('You cannot attack an empty hand.')
                elif right_p2 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    left_p1 = (left_p1 + right_p2) % 5
                    player = (player + 1) % 2
        elif move_p == 'rr':
            if player == 0:
                if right_p2 == 0:
                    print('You cannot attack an empty hand.')
                elif right_p1 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    right_p2 = (right_p2 + right_p1) % 5
                    player = (player + 1) % 2
            else:
                if right_p1 == 0:
                    print('You cannot attack an empty hand.')
                elif right_p2 == 0:
                    print('You cannot attack with an empty hand.')
                else:
                    right_p1 = (right_p1 + right_p2) % 5
                    player = (player + 1) % 2
        elif move_p == 'div':
            if player == 0:
                if (left_p1 == 0) & (right_p1 % 2 == 0) or ((left_p1 % 2 == 0) & (right_p1 == 0)):
                    new_value = max(left_p1, right_p1) // 2
                    left_p1, right_p1 = new_value, new_value
                    player = (player + 1) % 2
                else:
                    print('To use div, you ,ust have one empty hand and an even number on the other. Try again.')
            else:
                if (left_p2 == 0) & (right_p2 % 2 == 0) or ((left_p2 % 2 == 0) & (right_p2 == 0)):
                    new_value = max(left_p2, right_p2) // 2
                    left_p2, right_p2 = new_value, new_value
                    player = (player + 1) % 2
                else:
                    print('To use div, you must have one empty hand and an even number on the other. Try again.')
        else:
            print(f'{move_p} is not a valid move. Retry.')
    print(f'Player {(player+1) % 2 + 1} wins!')

