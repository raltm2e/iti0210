import operator, random


def pure_mc(position, my_side, N=200):
    initial_moves = moves(position)
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            res = simulate(position, my_side)
            if res == "WIN":
                win_counts[move] += 1
            elif res == "DRAW":
                win_counts[move] += 0.5
    return max(win_counts.items(), key=operator.itemgetter(1))[0]


def play_game(position, player_turn, player_side ="X"):
    playing = True
    while playing:
        if player_turn:
            print(position)
            print_board(position)
            move = get_player_move(position)
            player_turn = False
            position = make_move(position, move, player_side)
        else:
            #move = pure_mc(position, player_side)
            player_turn = True
        #position = make_move(position, move, player_side)
        if is_over(position) > 0:
            playing = False


def simulate(position, player_side):
    playing = True
    player_turn = True
    while playing:
        if player_turn:
            print(position)
            move = get_random_move(position)
            player_turn = False
        else:
            move = get_random_move(position)
            player_turn = True

        position = make_move(position, move, player_side)
        if is_over(position) > 0:
            playing = False
    if is_over(position) == 2:
        return "WIN"
    if is_over(position) == 3:
        return "DRAW"


def moves(position):
    moveList = [0, 1, 2, 3, 4, 5, 6]
    suitable_moves = []
    for move in moveList:
        print("Move", move)
        print(len(position[move]) < 6)
        if len(position[move]) < 6:
            suitable_moves.append(move)
    return suitable_moves


def make_move(position, move, player_side):
    if position[move] == [0]:
        position[move] = [player_side]
    else:
        position[move].append(player_side)
    return position


def is_over(position):
    # 0 - game continues; 1 - X wins; 2 - O wins; 3 - draw, no more moves
    horisontal_sum = get_horisontal_sum(position)
    diagonal_sum = get_diagonal_sum(position)
    if horisontal_sum > 0:
        return horisontal_sum
    if diagonal_sum > 0:
        return diagonal_sum
    for coordinate in position.values():
        if get_vertical_sum(coordinate) > 0:
            get_vertical_sum(coordinate)
    if len(moves(position)) == 0:
        return 3
    return 0


def get_vertical_sum(vertical_list):
    xCount = 0
    oCount = 0
    for element in vertical_list:
        if element == "X":
            xCount += 1
            oCount = 0
        elif element == "O":
            oCount += 1
            xCount = 0
    if xCount > 4:
        return 1
    elif oCount > 4:
        return 2
    return 0


def get_horisontal_sum(position):
    for i in range(len(position)):
        for j in range(len(position[i])):
            if i + 3 < len(position) and j < len(position[i + 1]) and j < len(position[i + 2]) and j < len(position[i + 3]):
                horisontal_list = [position[i][j], position[i + 1][j], position[i + 2][j], position[i + 3][j]]
                if get_vertical_sum(horisontal_list) > 0:
                    return get_vertical_sum(horisontal_list)
    return 0


def get_diagonal_sum(position):
    for i in range(len(position)):
        for j in range(len(position[i])):
            if i + 3 < len(position):
                if j + 1 < len(position[i + 1]) and j + 2 < len(position[i + 2]) and j + 3 < len(position[i + 3]):
                    diagonal_list = [position[i][j], position[i + 1][j + 1], position[i + 2][j + 2], position[i + 3][j + 3]]
                    if get_vertical_sum(diagonal_list) > 0:
                        return get_vertical_sum(diagonal_list)
                if j - 1 < len(position[i + 1]) and j - 2 < len(position[i + 2]) and j - 3 < len(position[i + 3]) and j - 3 > 0:
                    diagonal_list = [position[i][j], position[i + 1][j - 1], position[i + 2][j - 2], position[i + 3][j - 3]]
                    if get_vertical_sum(diagonal_list) > 0:
                        return get_vertical_sum(diagonal_list)
    return 0


def get_random_move(position):
    suitable_moves = moves(position)
    return random.choice(suitable_moves)


def get_player_move(position):
    while True:
        inputString = input("Sisesta käik (0-6): ")
        try:
            val = int(inputString)
            suitable_moves = moves(position)
            print(suitable_moves)
            if val in suitable_moves:
                return val
            print("Entered invalid move!")
        except ValueError:
            print("You entered string!")


def print_board(positions):
    for i in range(6, -1, -1):
        line = "|"
        for position in positions:
            if len(positions[position]) < i + 1:
                line += " "
            elif positions[position][i] == 0:
                line += " "
            else:
                line += str(positions[position][i])
        line += "|"
        print(line)
    print("|0123456|")

if __name__ == '__main__':
    position = {0: [0], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0], 6: [0]}
    play_game(position, True)
