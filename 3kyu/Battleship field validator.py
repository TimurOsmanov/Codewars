# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true
# if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
# Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid
# containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field.
# The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version.
# In this kata we will use Soviet/Russian version of the game.
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and
# 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.
# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
# This is all you need to solve this kata. If you're interested in more information about the game, visit this link.
def validate_battlefield(field):
    ships = {1: 0, 2: 0, 3: 0, 4: 0}
    ships_places = []
    dir_, count = 0, 1
    for n_r, row in enumerate(field):
        for n_c, col in enumerate(row):
            if col == 1:
                near_f = [(n_r + 1, n_c - 1), (n_r - 1, n_c - 1), (n_r - 1, n_c + 1), (n_r + 1, n_c + 1)]
                new_near_f = [(x, y) for x, y in near_f if 0 <= x < len(field[0]) and 0 <= y < len(field) and
                              (x, y) not in ships_places and field[x][y] == 1]
                if new_near_f:
                    return False
                if (n_r, n_c) not in ships_places:
                    ships_places.append((n_r, n_c))
                near = [(n_r, n_c - 1), (n_r, n_c + 1), (n_r - 1, n_c), (n_r + 1, n_c)]
                new_near = [(x, y) for x, y in near if 0 <= x < len(field[0]) and 0 <= y < len(field)
                            and (x, y) not in ships_places and field[x][y] == 1]
                if new_near:
                    dir_ = near.index(new_near[0])
                for x, y in near:
                    if 0 <= x < len(field[0]) and 0 <= y < len(field) and (x, y) not in ships_places:
                        neighbours1 = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
                        if field[x][y] == 1:
                            count += 1
                            ships_places.append((x, y))
                            new_near = [(x, y) for x, y in neighbours1 if 0 <= x < len(field[0])
                                        and 0 <= y < len(field) and (x, y) not in ships_places and field[x][y] == 1]
                            if new_near:
                                if neighbours1.index(new_near[0]) == dir_:
                                    near.append(new_near[0])
                if count in ships:
                    ships[count] += 1
                    count = 1
                else:
                    return False
    return True if ships == {1: 14, 2: 3, 3: 2, 4: 1} else False


battlefield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battlefield))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
# 1
#
# from collections import Counter
#
# MOVES = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1))
# VALID = {4:1, 3:2, 2:3, 1:4}
#
# def validateBattlefield(field):
#     return sum(map(sum,field))==20 and Counter(flood(list(map(list,field))))==VALID
#
# def flood(field, x=0, y=0):
#     while x<10 and not field[x][y]: x,y = divmod(10*x+y+1,10)
#     if x<10:
#         bag, found = {(x,y)}, set()
#         while bag:
#             found |= bag
#             for a,b in bag: field[a][b]=0
#             bag = {(a+dx,b+dy) for a,b in bag for dx,dy in MOVES if 0<=a+dx<10 and 0<=b+dy<10 and field[a+dx][b+dy]}
#         valid = 1 in {len(set(dim)) for dim in zip(*found)} and len(found)
#         yield valid
#         if valid: yield from flood(field,x,y)
#
# 2
#
# def validateBattlefield(field):
#     n, m = len(field), len(field[0])
#
#     def cell(i, j):
#         if i < 0 or j < 0 or i >= n or j >= m:
#             return 0
#         return field[i][j]
#
#     def find(i, j):
#         if cell(i + 1, j - 1) or cell(i + 1, j + 1):
#             return 10086
#         if cell(i, j + 1) and cell(i + 1, j):
#             return 10086
#         field[i][j] = 2
#         if cell(i, j + 1):
#             return find(i, j + 1) + 1
#         if cell(i + 1, j):
#             return find(i + 1, j) + 1
#         return 1
#
#     num = [0] * 5
#     for i in range(n):
#         for j in range(m):
#             if cell(i, j) == 1:
#                 r = find(i, j)
#                 if r > 4:
#                     return False
#                 num[r] += 1
#     [tmp, submarines, destroyers, cruisers, battleship] = num
#     return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4
