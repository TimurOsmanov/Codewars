import itertools
import functools


def permutations(string):
    combinations = []
    for x in itertools.permutations(string):
        combinations.append(functools.reduce(lambda z, y: z + y, x))
    return sorted(set(combinations))

# def permutations(string):
#     return list("".join(p) for p in set(itertools.permutations(string)))


print(permutations('aabb'))

