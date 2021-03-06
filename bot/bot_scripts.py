import random
import copy

def check(table, player):
    for i in range(10):
        for j in range(6):
            if table[i][j] == table[i][j+1] == table[i][j+2] == table[i][j+3] == table[i][j+4] == player or table[j][i]\
                    == table[j+1][i] == table[j+2][i] == table[j+3][i] == table[j+4][i] == player:
                return 1
    for i in range(6):
        for j in range(6):
            if table[i][j] == table[i+1][j+1] == table[i+2][j+2] == table[i+3][j+3] == table[i+4][j+4] == player:
                return 1
    for i in range(4, 10):
        for j in range(6):
            if table[i][j] == table[i-1][j+1] == table[i-2][j+2] == table[i-3][j+3] == table[i-4][j+4] == player:
                return 1
    for i in range(10):
        for j in range(10):
            if table[i][j] == 0:
                return 0
    return 2              # draw


def choice_of_move(table):
    possible_moves = []
    for i in range(10):
        for j in range(10):
            if table[i][j] == 0:
                possible_moves.append((i, j))

    while len(possible_moves) > 0:
        temp_table = copy.copy(table)
        index = random.randint(0, len(possible_moves) - 1)
        move = possible_moves[index]
        temp_table[move[0]][move[1]] = -1
        if check(temp_table, -1) != 1:
            break
        else:
            possible_moves.pop(index)
    return move


