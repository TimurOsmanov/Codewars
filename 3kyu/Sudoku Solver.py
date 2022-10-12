# Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of
# the 2D puzzle array, with the value 0 representing an unknown square.
#
# The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume
# and test possibilities on unknowns) and can be solved with a brute-force approach.
#
# For Sudoku rules, see the Wikipedia article.


def sudoku(puzzle):
    correct, rows, cols, squares = list(range(1, 10)), [x for x in puzzle], [x for x in zip(*puzzle)], {}
    for i in range(3):
        for j in range(3):
            temp = []
            for row in puzzle[i * 3: (i + 1) * 3]:
                temp += row[j * 3: (j + 1) * 3]
            squares[(tuple(range(i * 3, (i + 1) * 3)), tuple(range(j * 3, (j + 1) * 3)))] = temp

    cells, square_pos = [], ()
    for num_row, row in enumerate(puzzle):
        for num_col, cell in enumerate(row):
            if cell == 0:
                for x in squares.keys():
                    i, j = x
                    if num_row in i and num_col in j:
                        square_pos = x
                cells.append(
                    (num_row, num_col, set(correct) - set(row) - set(cols[num_col]) - set(squares[square_pos])))

    cells_to_update = [x for x in cells if len(x[2]) == 1]
    for update_cell in cells_to_update:
        puzzle[update_cell[0]][update_cell[1]] = list(update_cell[2])[0]
    if cells:
        sudoku(puzzle)
    return puzzle


test = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sol_ = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]

print(sudoku(test))

########################################################################################################################
############################################## best practice ###########################################################
########################################################################################################################
# def sudoku(P):
#
#     for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:
#
#         rr, cc = (row // 3) * 3, (col // 3) * 3
#
#         use = {1,2,3,4,5,6,7,8,9} - ({P[row][c] for c in range(9)} | {P[r][col] for r in range(9)} | {P[rr+r][cc+c] for r in range(3) for c in range(3)})
#
#         if len(use) == 1:
#             P[row][col] = use.pop()
#             return sudoku(P)
#     return P
