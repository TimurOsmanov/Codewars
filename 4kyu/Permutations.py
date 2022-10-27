# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.
# * With input 'a'
# * Your function should return: ['a']
# * With input 'ab'
# * Your function should return ['ab', 'ba']
# * With input 'aabb'
# * Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
import itertools
import functools


def permutations(string):
    combinations = []
    for x in itertools.permutations(string):
        combinations.append(functools.reduce(lambda z, y: z + y, x))
    return sorted(set(combinations))


print(permutations('aabb'))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# import itertools
# def permutations(string):
#     return list("".join(p) for p in set(itertools.permutations(string)))
#
#
# print(permutations('aabb'))
