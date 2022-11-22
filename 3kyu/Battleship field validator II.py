# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true
# if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
# Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid
# containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field.
# The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version.
# In this kata we will use Soviet/Russian version of the game.
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2)
# and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.
# The ship cannot overlap, but can be contact with any other ship.
# The description likes Battleship field validator Kata, the only difference is the rule 3.
from itertools import combinations


def validate_battlefield(battlefield):
    fleet = {4: 1, 3: 2, 2: 3, 1: 4}
    possible_ships = {}
    ships_counter = 0

    def add_possible_ship(ship_position, ship):
        if ship not in possible_ships:
            possible_ships[ship] = [ship_position]
        else:
            if ship_position not in possible_ships[ship]:
                possible_ships[ship].append(ship_position)

    def check_down(row_num, col_num, i):
        down = None if row_num + 1 > len(battlefield) - 1 else battlefield[row_num + 1][col_num]
        if down:
            check_down(row_num + 1, col_num, i + 1)
            ship_position = [(row_num - cell, col_num) for cell in range(i)]
            add_possible_ship(ship_position, i)
        else:
            ship_position = [(row_num - cell, col_num) for cell in range(i)]
            add_possible_ship(ship_position, i)

    def check_right(row_num, col_num, i):
        right = None if col_num + 1 > len(battlefield) - 1 else battlefield[row_num][col_num + 1]
        if right:
            check_right(row_num, col_num + 1, i + 1)
            ship_position = [(row_num, col_num - cell) for cell in range(i)]
            add_possible_ship(ship_position, i)
        else:
            ship_position = [(row_num, col_num - cell) for cell in range(i)]
            add_possible_ship(ship_position, i)

    for row_num, row in enumerate(battlefield):
        for col_num, cell in enumerate(row):
            if cell == 1:
                check_down(row_num, col_num, 1)
                check_right(row_num, col_num, 1)
                ships_counter += 1

    if {1, 2, 3, 4} & set([x for x in possible_ships]) != {1, 2, 3, 4}:
        return False

    for battleship in possible_ships[4]:
        temp_cruiser = []
        for cruiser in possible_ships[3]:
            if all([cell not in battleship for cell in cruiser]):
                temp_cruiser.append(cruiser)
        possible_places = [[battleship, cruiser1, cruiser2] for cruiser1, cruiser2 in combinations(temp_cruiser, 2)
                           if all([cell not in cruiser2 for cell in cruiser1])]

        for place in possible_places:
            temp_destroyer = []
            occupied = [cell for ship in place for cell in ship]
            for destroyer in possible_ships[2]:
                if all([cell not in occupied for cell in destroyer]):
                    temp_destroyer.append(destroyer)

            possible_places1 = [[*place, destr1, destr2, destr3] for destr1, destr2, destr3 in
                                combinations(temp_destroyer, 3) if all(cell not in destr2 + destr3 for cell in destr1)
                                and all(cell not in destr1 + destr3 for cell in destr2)
                                and all(cell not in destr1 + destr2 for cell in destr3)]
            if possible_places1:
                for place in possible_places1:
                    occupied1 = [cell for ship in place for cell in ship]
                    submarines = [sub[0] for sub in possible_ships[1] if sub[0] not in occupied1]
                    if ships_counter == 20 and len(occupied1 + submarines) == 20:
                        return True
    return False


print(validate_battlefield([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                            [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0], ]))

# True
print(validate_battlefield([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

# True
print(validate_battlefield([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

# False
print(validate_battlefield([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

# False
print(validate_battlefield([[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                            [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
# 1
# import numpy as np
# from itertools import combinations
#
# def validate_battlefield(field):
#     return validate(np.array(field), [(1,4),(2,3),(3,2)], 20)
#
# def validate(field, ships, expected):
#     if field.sum() != expected: return False
#     elif not ships: return True    # single-unit ships can be anywhere, so we can shortcut
#
#     # We are looking for (n) ships of length (size).
#     (n,size),remaining = ships[0], ships[1:]
#
#     # Find horizontal/vertical slices of the appropriate length containing all ones ...
#     slices = filter(all, (f[i,j:j+size] for f in (field,field.T) for (i,j) in zip(*np.where(f))))
#
#     # ... and try zeroing-out (n) of them at a time to find a valid combination.
#     # If the recursive check fails, we backtrack by setting the slices back to one.
#     return any(
#         assign(s,0) or validate(field, remaining, expected-n*size) or assign(s,1)
#             for s in combinations(slices, n)
#     )
#
# def assign(slices, x):
#     # Set the value of all array slices in a collection
#     for arr in slices: arr[:] = x
#
# 2
# def validateBattlefield(field):
#     return battle(set([(r, c) for c in range(10) for r in range(10) if field[r][c]]), [1,1,1,1,2,2,2,3,3,4])
#
# def battle(grid, fleet):
#     return sum(fleet) == len(grid) and (fleet == [] or any(battle(grid - p, fleet[:-1]) for p in possibles(grid, fleet[-1])))
#
# def possibles(grid, ship):
#     return [set(p) for p in [[(r+i,c) for i in range(ship)] for r, c in grid] + [[(r,c+i) for i in range(ship)] for r,c in grid] if set(p) <= grid]