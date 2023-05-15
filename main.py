def get_print(number_l: int, number_r: int, player_id: int) -> list:
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


def is_valid(move: str, l_player: int, r_player: int, l_opponent: int, r_opponent: int) -> bool:
    '''
    Verifie la validité du mouvement (règles de jeu).
    :param move: Le mouvement fait par "player" contre "opponent".
    :param l_player: nombre de doigts de la main gauche du joueur attaquant
    :param r_player: nombre de doigts de la main droite du joueur attaquant
    :param l_opponent: nombre de doigts de la main gauche du joueur attaqué
    :param r_opponent: nombre de doigts de la main droite du joueur attaqué
    :return: answer (bool)
    '''
    if move == 'll':
        if l_player == 0:
            print('You cannot attack with an empty hand.')
            answer = False
        elif l_opponent == 0:
            print('You cannot attack an empty hand.')
            answer = False
        else:
            answer = True
    elif move == 'lr':
        if l_player == 0:
            print('You cannot attack with an empty hand.')
            answer = False
        elif r_opponent == 0:
            print('You cannot attack an empty hand.')
            answer = False
        else:
            answer = True
    elif move == 'rl':
        if r_player == 0:
            print('You cannot attack with an empty hand.')
            answer = False
        elif l_opponent == 0:
            print('You cannot attack an empty hand.')
            answer = False
        else:
            answer = True
    elif move == 'rr':
        if r_player == 0:
            print('You cannot attack with an empty hand.')
            answer = False
        elif r_opponent == 0:
            print('You cannot attack an empty hand.')
            answer = False
        else:
            answer = True
    elif move == 'div':
        if (l_player == 0) & (r_player % 2 == 0) or ((l_player % 2 == 0) & (r_player == 0)):
            answer = True
        else:
            print('To use div, you must have one empty hand and an even number on the other. Try again.')
            answer = False
    else:
        print(f'{move} is not a valid move.')
        answer = False
    return answer


def move_player(move: str, l_player: int, r_player: int, l_opponent: int, r_opponent: int) -> tuple:
    '''
    Fonction pour determiner les nouvelles mains.
    :param move: Le mouvement fait par "player" contre "opponent". Doit avoir été validé par
    la fonction is_valid qui contient les règles du jeu.
    :param l_player: nombre de doigts de la main gauche du joueur attaquant
    :param r_player: nombre de doigts de la main droite du joueur attaquant
    :param l_opponent: nombre de doigts de la main gauche du joueur attaqué
    :param r_opponent: nombre de doigts de la main droite du joueur attaqué
    :return: l_player, r_player, l_opponent, r_opponent
    '''
    if move == 'll':
        l_opponent = (l_opponent + l_player) % 5
    elif move == 'lr':
        r_opponent = (r_opponent + l_player) % 5
    elif move == 'rl':
        l_opponent = (l_opponent + r_player) % 5
    elif move == 'rr':
        r_opponent = (r_opponent + r_player) % 5
    else:
        new_value = max(l_player, r_player) // 2
        l_player, r_player = new_value, new_value
    return l_player, r_player, l_opponent, r_opponent


def move_p(move: str, lp1: int, rp1: int, lp2: int, rp2: int, p: int) -> tuple:
    '''
    Vérifie si le mouvement est valide. S'il l'est, l'effectue et change l'indicateur de tour de jeu.
    Sinon retourne les mêmes valeurs qu'à l'entrée, permettant au joueur de fournir un mouvement valide.
    :param move: Le mouvement fait par joueur identifié selon l'indicateur p.
    :param lp1: nombre de doigts de la main gauche du joueur 1
    :param rp1: nombre de doigts de la main droite du joueur 1
    :param lp2: nombre de doigts de la main gauche du joueur 2
    :param rp2: nombre de doigts de la main droite du joueur 2
    :param p: indicateur du joueur attaquant. 0 -> joueur 1, 1 -> joueur 2
    :return: lp1, rp1, lp2, rp2, p
    '''
    if p == 0:  # Le joueur attaquant est joueur 1
        if is_valid(move, lp1, rp1, lp2, rp2):
            lp1, rp1, lp2, rp2 = move_player(move, lp1, rp1, lp2, rp2)
            p = (p + 1) % 2
    else:  # Attention à l'ordre ici, le joueur attaquant est joueur 2
        if is_valid(move, lp2, rp2, lp1, rp1):
            lp2, rp2, lp1, rp1 = move_player(move, lp2, rp2, lp1, rp1)
            p = (p + 1) % 2
    return lp1, rp1, lp2, rp2, p


if __name__ == '__main__':
    left_p1, right_p1, left_p2, right_p2 = 1, 1, 1, 1
    player = 0
    name_p1, name_p2 = 'Player 1', 'Player 2'
    r = input('Do you wish to enter player names? (y/n)').lower()
    if r == 'y':
        name_p1 = input("Player 1's name: ")
        name_p2 = input("Player 2's name: ")
        while (name_p1 == '') or (name_p2 == '') or (name_p1 == name_p2):
            print('Invalid names. Names cannot be empty or identical. Try again.')
            name_p1 = input("Player 1's name: ")
            name_p2 = input("Player 2's name: ")
    elif r == 'n':
        print("OK! Default names used.")
    else:
        print(f"{r} is not valid. Using default names.")
    while ((left_p1 != 0) or (right_p1 != 0)) and ((left_p2 != 0) or (right_p2 != 0)):
        print('Current hands:')
        print(name_p2.center(44))
        print(f'       r ({right_p2})                    l ({left_p2})')
        p2_hands = get_print(right_p2, left_p2, 1)
        for line in p2_hands:
            print(line)
        print("------------------------------------------------")
        p1_hands = get_print(left_p1, right_p1, 0)
        for line in p1_hands:
            print(line)
        print(f'       l ({left_p1})                    r ({right_p1})')
        print(name_p1.center(44))
        name = name_p1 if player == 0 else name_p2
        m = input(f'Hi {name}! What is your move? (ll/lr/rl/rr/div)').lower()
        left_p1, right_p1, left_p2, right_p2, player = move_p(m, left_p1, right_p1, left_p2, right_p2, player)

    name_win = name_p2 if player == 0 else name_p1
    print(f'{name_win} wins!')

