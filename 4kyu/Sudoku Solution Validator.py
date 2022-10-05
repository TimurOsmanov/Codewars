import numpy as np

d = []
f = []
e = []
i = 1


def sub_grids(matrix):
    global d
    global f
    global e
    global i
    for x in matrix:
        d.append(x[0:3])
        for z in x[0:3]:
            matrix[matrix.index(x)].remove(z)
    if matrix[0]:
        sub_grids(matrix)
    sub_l = []
    end_l = []
    for x in d:
        if i <= 3:
            for a in x:
                sub_l.append(a)
            i += 1
        else:
            end_l.append(sub_l)
            sub_l = []
            for a in x:
                sub_l.append(a)
            i = 2
    end_l.append(sub_l)
    return end_l[1:]


def valid_solution(board):
    board_old = board.copy()
    board = np.array(board)
    a = list(map(lambda x: sum(x) == 45 and 0 not in x, board))
    b = list(map(lambda x: sum(x) == 45 and 0 not in x, board.transpose()))
    c = list(map(lambda x: sum(x) == 45 and 0 not in x, sub_grids(board_old)))
    if all(b) and all(a) and all(c):
        return True
    else:
        return False


print(valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]))

# best practice
# correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def validSolution(board):
#     # check rows
#     for row in board:
#         if sorted(row) != correct:
#             return False
#
#     # check columns
#     for column in zip(*board):
#         if sorted(column) != correct:
#             return False
#
#     # check regions
#     for i in range(3):
#         for j in range(3):
#             region = []
#             for line in board[i*3:(i+1)*3]:
#                 region += line[j*3:(j+1)*3]
#
#             if sorted(region) != correct:
#                 return False
#
#     # if everything correct
#     return True
