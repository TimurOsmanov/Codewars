import numpy as np
from itertools import accumulate as ac


def sorting(line, player):
    s = 0
    for x in line:
        if x == player:
            s += 1
            if s == 4:
                return s
        else:
            s = 0


def func(pieces_position_list):
    raw_list = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []}
    for move in pieces_position_list:
        col, player = move.split('_')
        raw_list[col].append(player)
    for col in raw_list:
        if len(raw_list[col]) != 6:
            for null in range(6 - len(raw_list[col])):
                raw_list[col].append(0)
    horizontal = np.array([raw_list[col] for col in sorted(raw_list)])
    vertical = horizontal.transpose()
    diagonal1 = [np.diagonal(horizontal, offset=offset, axis1=0, axis2=1) for offset in list(range(-3, 3))]
    diagonal2 = [np.diagonal(np.fliplr(horizontal), offset=offset, axis1=1, axis2=0) for offset in list(range(-3, 3))]
    all_lines = []
    for ans_list in horizontal, vertical, diagonal1, diagonal2:
        for line in ans_list:
            all_lines.append(line)
    i = 0
    for line in all_lines:
        i += 1

        if i == len(all_lines):
            if sorting(line, 'Yellow') == 4:
                return 'Yellow'
            elif sorting(line, 'Red') == 4:
                return 'Red'
            else:
                return 'Draw'
        else:
            if sorting(line, 'Yellow') == 4:
                return 'Yellow'
            elif sorting(line, 'Red') == 4:
                return 'Red'


def who_is_winner(pieces_position_list):
    pieces_position_list = [[x] for x in pieces_position_list]
    moves_list = [x for x in ac(pieces_position_list)]
    i = 0
    for x in moves_list:
        i += 1
        if i == len(moves_list):
            return func(x)
        else:
            if func(x) != 'Draw':
                return func(x)


a = who_is_winner(['C_Red', 'E_Yellow', 'F_Red', 'F_Yellow', 'E_Red', 'A_Yellow', 'A_Red', 'C_Yellow', 'E_Red', 'D_Yellow', 'G_Red', 'C_Yellow', 'A_Red', 'G_Yellow', 'A_Red', 'B_Yellow', 'G_Red', 'D_Yellow', 'D_Red', 'A_Yellow', 'C_Red', 'G_Yellow', 'C_Red', 'E_Yellow', 'B_Red', 'C_Yellow'])
print(a)
# best practice
# import numpy as np
# from scipy.signal import convolve2d
# def who_is_winner(pieces_position_list):
#     arr = np.zeros((7,6), int)
#     for a in pieces_position_list:
#         pos, color = a.split('_')
#         pos = ord(pos) - ord('A')
#         val = (-1,1)[color == 'Red']
#         arr[pos, np.argmin(arr[pos] != 0)] = val
#         t_arr = val * arr
#         if any(np.max(cv) == 4 for cv in (convolve2d(t_arr, [[1,1,1,1]], 'same'),
#                                           convolve2d(t_arr, [[1],[1],[1],[1]], 'same'),
#                                           convolve2d(t_arr, [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]], 'same'),
#                                           convolve2d(t_arr, [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]], 'same'))):
#             return color
#     return 'Draw'