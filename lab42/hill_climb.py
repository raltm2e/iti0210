
def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        print(pos.best_move())
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


class NQPosition:
    def __init__(self, N):
        self.N = N
        self.queenList = []
        for i in range(N):
            self.queenList.append(0)


    def value(self):
        conflict_number = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.queenList[i] == self.queenList[j]:
                    conflict_number += 1
        return conflict_number


    def make_move(self, move):
        xCoord = move[0]
        yCoord = move[1]
        self.queenList[xCoord] = yCoord


    def best_move(self):
        possible_moves = []
        for i in range(self.N):
            for j in range(1, self.N):
                possible_moves.append((i, self.queenList[i] + j))

        best_conflict_value = 99999
        best_move = ()
        print(len(best_move))
        for move in possible_moves:
            nqPosition = NQPosition(self.N)
            nqPosition.make_move(move)
            conflict_value = nqPosition.value()
            if conflict_value < best_conflict_value:
                best_conflict_value = conflict_value
                best_move = move

        return best_move, best_conflict_value
        #find the best move and the value function after making that move
        #return move, value


pos = NQPosition(4)
print("Initial position value", pos.value())
best_pos, best_value = hill_climbing(pos)
# print("Final value", best_value)
# if best_value is 0, we solved the problem