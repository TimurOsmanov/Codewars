# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
# (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
#
# Empty positions are marked . .
# Walls are marked W .
# Start and exit positions are empty in all test cases.
def p_moves(x, y, maze):
    north = () if y - 1 == -1 else (x, y - 1)
    east = () if x + 1 == len(maze[0]) else (x + 1, y)
    south = () if y + 1 == len(maze) else (x, y + 1)
    west = () if x - 1 == - 1 else (x - 1, y)
    moves = [(maze[c[1]][c[0]], c) if c else None for c in (north, east, south, west)]
    possible_moves = [m[1] for m in [m for m in moves if m] if m[0] == '.']
    return possible_moves


def move(maze, pathes, path):
    global ans
    end_point = (len(maze[0]) - 1, len(maze) - 1)
    if not pathes:
        ans = False
        return False
    if end_point in pathes:
        ans = True
        return True
    new_pathes = set()
    for x in pathes:
        path.add(x)
        new_ = [new_pathes.add(x) for x in p_moves(x[0], x[1], maze) if x not in path]
        a = [path.add(x) for x in new_pathes]
    move(maze, new_pathes, path)


def path_finder(maze):
    global ans
    maze, pathes, path = maze.split('\n'), [(0, 0)], set()
    move(maze, pathes, path)
    return ans


a = '\n'.join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W."])

a2 = '\n'.join([
    "...WW",
    "...WW",
    "....W",
    ".W..W",
    "..W.."])

a3 = '\n'.join([
    "..W.",
    ".W.W",
    "..WW",
    "...."])

a5 = '\n'.join([
    ".W...",
    ".W...",
    ".W.W.",
    "...WW",
    "...W.",
    ])


a4 = '\n'.join([
                ".W........W...W........W..W.....W......WW.....WW.",
                "..WWW.WW.WWW.W...W.............W...W.............",
                ".........WW...W..W....W.W..W..W........W.........",
                "............W.W.W..W......W.W...WW.......W..W...W",
                "WWWW.WW...W.....W...W...W...WW.W.W....W...W..W...",
                ".WW.W.......WWW.W..W.....W..WWW.....WW.W..W.WW.WW",
                "......W..W..W...W...W.W.W..W.WW....W.W..WW..W.WW.",
                "........W.WW.........W..W..W...WW...WW..W......W.",
                "......W.W.WW.W.W...W...W...W..W..W..WW....W..W..W",
                "W......WWW.W.W.......W..WWW......WW.W............",
                "W..W............WW...W..W....W..W.......W....W...",
                "W...WWW.WW.....WW.....W.W..........W.W.W.....WW..",
                "WW.W.....W.W.W..........W....W.W.W.W...WW.WWW....",
                "...WWWWWW.WW...W..W.....W......WWW...W.W....W.W..",
                ".W.W..W....W..W.......W..W..W....WW......WW......",
                "...W.W.WWW........W....WW....W.W....W..W.....W.W.",
                "W.W........W.........WWW..W.WW...W.........W..W.W",
                ".......W.W....W.WW.....W.....W.W....W..W..W..W...",
                "W...WW.WWWWWW..WWWWWW..WWWW.WW.W........WW.WW.WW.",
                "W...W....W.....W.W..W....................W...W..W",
                "..........WW.W...W.W..WW...W.W.W...W.W...W.......",
                "...W..W.........W........W...W..W.WW.W...........",
                "...W.....W.W....WWW.WW....W......W....W.W...W..W.",
                ".W....W.......W......W......W....WWWW..W........W",
                ".......W..WW...W.W...W...W.W...WW....WW....W.....",
                "WW.....W.W..WW.......W.W....W.W.......WW.....W...",
                ".W......W....W.......W..W...WWW..WW..W...........",
                "W......WWWW.W.W.W.W..W.............WW.......WWW.W",
                "..W.W.....W.........W......W.....W..............W",
                "W.......W..W.W.WW...............WWW.W...W.....W..",
                "W..W.W..W............W.W.......W..WWW.....W.....W",
                "WW...............WW..W..W..........W......WWWW...",
                "..W.W........W.WWWW....W..W..W.W......WWW........",
                "......WW..WW..W.W..W.W..W.W.....W...W.W....W..W..",
                "W.W.WWW.WWW..W.....WW........W......W...W.W......",
                "..W..........W..W...W....W.W.....WW.W...W.....W..",
                ".W....W.W.W.....W..........W......WW..........W.W",
                "W....W.....W....W....WW.WW...W.W..W.W..WW.......W",
                "......W...W......W.........W..............WW.W.W.",
                "............W..W....W..W.WW.W.....WW.WW.WW...W.W.",
                ".....W.......W.........W...W.W..W.W...W....W.....",
                "W.WW...WW..WW...........W..WW....W...WWW.....W.W.",
                "W..W.W...W....W.W.W......WW...W.....W...W..WW.WWW",
                "W.W.....W..W.....W.....W.W....WW.....W.....W...WW",
                "..............W........W...WW.W........W.W..WWW.W",
                "...W....W......W..W.W.....W..W.W.W..W.......W.WW.",
                "....WW........W........W..W........WW..W.W.W..W..",
                "...W.W....WW.W...W..W.W....WWW..W......WW....W...",
                ".W....WWW..W.....W.W.....WW...W...W....W........."])

print(path_finder(a4))

# best practice
# 1
#
# def path_finder(maze):
#     matrix = list(map(list, maze.splitlines()))
#     stack, length = [[0, 0]], len(matrix)
#     while len(stack):
#       x, y = stack.pop()
#       if matrix[x][y] == '.':
#         matrix[x][y] = 'x'
#         for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
#           if 0 <= x < length and 0 <= y < length:
#             stack.append((x, y))
#     return matrix[length-1][length-1] == 'x'
# 2
#
# def path_finder(maze):
#     maze = [list(level) for level in maze.split("\n")]
#     N = len(maze)
#     Q = [(0, 0)]
#
#     while Q:
#         x, y = Q.pop(0)
#         if x >= 0 and y >= 0 and x < N and y < N:
#             if x == N-1 and y == N-1:
#                 return True
#             if maze[y][x] == '.':
#                 maze[y][x] = 'W'
#                 directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#                 for dx, dy in directions:
#                     Q.append((x + dx, y + dy))
#     return False