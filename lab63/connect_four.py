import operator, random


def pure_mc(positions_list, my_side, N=200):
    initial_moves = moves(positions_list)
    win_counts = dict((move, 0) for move in initial_moves)
    for move in initial_moves:
        for i in range(N):
            positions_list_copy = positions_list.copy()
            res = simulate(positions_list_copy, my_side)
            if res == "WIN":
                win_counts[move] += 1
            elif res == "DRAW":
                win_counts[move] += 0.5
    print("Win counts: ", win_counts)
    return max(win_counts.items(), key=operator.itemgetter(1))[0]


def play_game(positions_list, player_turn, player_side ="X"):
    playing = True
    oponent_side = "X"
    if player_side == "X":
        oponent_side = "O"
    while playing:
        if player_turn:
            print(positions_list)
            print_board(positions_list)
            move = get_player_move(positions_list)
            player_turn = False
            positions_list = make_move(positions_list, move, player_side)
        else:
            move = pure_mc(positions_list, oponent_side)
            player_turn = True
            positions_list = make_move(positions_list, move, oponent_side)
        if is_over(positions_list) > 0:
            playing = False


def simulate(positions_list, player_side):
    playing = True
    player_turn = True
    oponent_side = "X"
    if player_side == "X":
        oponent_side = "O"
    while playing:
        if player_turn:
            move = get_random_move(positions_list)
            player_turn = False
            positions_list = make_move(positions_list, move, player_side)
        else:
            move = get_random_move(positions_list)
            player_turn = True
            positions_list = make_move(positions_list, move, oponent_side)
        if is_over(positions_list) > 0:
            playing = False
    if is_over(positions_list) == 2:
        return "WIN"
    if is_over(positions_list) == 3:
        return "DRAW"
    else:
        return "LOSE"


def moves(positions_list):
    moveList = [0, 1, 2, 3, 4, 5, 6]
    suitable_moves = []
    for move in moveList:
        if len(positions_list[move]) < 6:
            suitable_moves.append(move)
    return suitable_moves


def make_move(positions_list, move, player_side):
    if positions_list[move] == [0]:
        positions_list[move] = [player_side]
    else:
        positions_list[move].append(player_side)
    return positions_list


def is_over(positions_list):
    # 0 - game continues; 1 - X wins; 2 - O wins; 3 - draw, no more moves
    horisontal_sum = get_horisontal_sum(positions_list)
    diagonal_sum = get_diagonal_sum(positions_list)
    if horisontal_sum > 0:
        return horisontal_sum
    if diagonal_sum > 0:
        return diagonal_sum
    for coordinate in positions_list.values():
        if get_vertical_sum(coordinate) > 0:
            return get_vertical_sum(coordinate)
    if len(moves(positions_list)) == 0:
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
    if xCount >= 4:
        return 1
    elif oCount >= 4:
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
