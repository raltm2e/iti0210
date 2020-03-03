import random, time

def hill_climbing(position):
    current_value = position.value()
    while True:
        move, new_value = position.best_move()
        if new_value >= current_value:
            # no improvement, give up
            return position, current_value
        else:
            # position improves, keep searching
            current_value = new_value
            print("Made move: ", move, new_value)
            position.make_move(move)
            print(position.queenList)


class NQPosition:
    def __str__(self) -> str:
        return str(self.queenList)

    def __init__(self, N):
        self.N = N
        self.queenList = []
        self.previousX = 9999
        self.previousY = 9999
        self.move_number = 0
        for i in range(N):
            self.queenList.append(0)


    def value(self):
        conflict_number = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.queenList[i] == self.queenList[j]:
                    conflict_number += 1
                offset = j - i
                if self.queenList[i] == self.queenList[j] - offset or self.queenList[i] == self.queenList[j] + offset:
                    conflict_number += 1
        return conflict_number


    def make_move(self, move):
        xCoord = move[0]
        yCoord = move[1]
        self.previousX = xCoord
        self.previousY = self.queenList[xCoord]
        self.move_number += 1
        self.queenList[xCoord] = yCoord

    def revert_move(self):
        self.queenList[self.previousX] = self.previousY
        self.move_number -= 1


    def best_move(self):
        possible_moves = []
        for i in range(self.N):
            for j in range(1, self.N):
                possible_moves.append((i, self.queenList[i] + j))
        best_conflict_value = 99999
        best_moves = []
        for move in possible_moves:
            self.make_move(move)
            conflict_value = self.value()
            if conflict_value < best_conflict_value:
                best_conflict_value = conflict_value
                best_moves = [move]
            elif conflict_value == best_conflict_value:
                best_moves.append(move)
            self.revert_move()
        return best_moves[random.randint(0, len(best_moves) - 1)], best_conflict_value


position = NQPosition(4)
print("Initial position conflict number:", position.value())
start_time = time.time() * 1000
best_pos, best_value = hill_climbing(position)
end_time = time.time() * 1000
print("Final position: ", best_pos)
print("Final value", best_value)
print("Time elapsed in milliseconds: ", end_time - start_time)
