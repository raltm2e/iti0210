
def pure_mc(position, my_side, N=200):
    # kõik käigud algseisus
    initial_moves = moves(position)
    # loendurid iga käigu jaoks
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            # mängi juhuslikult seis kuni lõpuni
            res = simulate(position, move, my_side)
            if res == "WIN":
                win_counts[move] += 1
            elif res == "DRAW":
                win_counts[move] += 0.5

    # leia suurima võitude arvuga käik, tagasta


def play_game(position, player_turn, player_side ="X"):
    playing = True
    while playing:
        if player_turn:
            print(position)
            print_board(position)
            move = get_player_move()
            player_turn = False
            position = make_move(position, move, player_side)
        else:
            #move = pure_mc(position, player_side)
            player_turn = True

        # position = make_move(position, move, player_side)
        if is_over(position):
            playing = False

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


def moves(position):
    moveList = [0, 1, 2, 3, 4, 5, 6]
    for move in moveList:
        if len(position[move]) >= 6:
            moveList.remove(move)
    return moveList


def make_move(position, move, player_side):
    if position[move] == [0]:
        position[move] = [player_side]
    else:
        position[move].append(player_side)
    return position


def is_over(position):
    if get_horisontal_sum(position):
        return True
    if get_diagonal_sum(position):
        return True
    for coordinate in position.values():
        if get_vertical_sum(coordinate) is True:
            return True
    return False


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
    if xCount < 4 and oCount < 4:
        return False
    return True


def get_horisontal_sum(position):
    for i in range(len(position)):
        for j in range(len(position[i])):
            if i + 3 < len(position) and j < len(position[i + 1]) and j < len(position[i + 2]) and j < len(position[i + 3]):
                horisontal_list = [position[i][j], position[i + 1][j], position[i + 2][j], position[i + 3][j]]
                if get_vertical_sum(horisontal_list):
                    return True
    return False


def get_diagonal_sum(position):
    for i in range(len(position)):
        for j in range(len(position[i])):
            if i + 3 < len(position):
                if j + 1 < len(position[i + 1]) and j + 2 < len(position[i + 2]) and j + 3 < len(position[i + 3]):
                    diagonal_list = [position[i][j], position[i + 1][j + 1], position[i + 2][j + 2], position[i + 3][j + 3]]
                    if get_vertical_sum(diagonal_list):
                        return True
                if j - 1 < len(position[i + 1]) and j - 2 < len(position[i + 2]) and j - 3 < len(position[i + 3]) and j - 3 > 0:
                    diagonal_list = [position[i][j], position[i - 1][j - 1], position[i - 2][j - 2], position[i - 3][j - 3]]
                    if get_vertical_sum(diagonal_list):
                        return True
    return False


def simulate(position, move, my_side):
    pass


def get_player_move():
    while True:
        inputString = input("Sisesta käik (0-6): ")
        try:
            val = int(inputString)
            if 0 <= val <= 6:
                return val
            print("Entered invalid move!")
        except ValueError:
            print("You entered string!")


if __name__ == '__main__':
    position = {0: [0], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0], 6: [0]}
    play_game(position, True)
