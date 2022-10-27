# In this kata we have to calculate products and sums using the values of an array with an arbitrary number
# of non-zero integers (positive and/or negative). Each number in the array occurs once, i.e. they are all unique.
#
# You need to implement a function eval_prod_sum(arr, num_fact, num_add, max_val)
# that takes the following four arguments:
#
# 1. A list/array of integers [x1,x2,x3,…,xn] of arbitrary length n where xi≠0

# 2. A positive integer num_fact, which is the number of array elements that combine to form individual products.
# For example, given an array [a, b, c, d] and num_fact = 3, the products would be a*b*c, a*b*d, a*c*d, b*c*d
#
# 3. A positive integer num_add, which is the number of previously produced products (see 2.)
# that combine to form individual sums.
# Continuing the previous example, given num_add = 2, the sums would be a*b*c + a*b*d, a*b*c + a*c*d, ..., a*c*d + b*c*d
#
# 4. An integer max_val, against which the previously produced sums will be compared to produce the following results:
#
# smaller, the number of sums that are smaller than max_val
#
# equal, the number of sums that are equal to max_val
#
# larger, the number of sums that are larger than max_val
import itertools
import functools


def eval_prod_sum(lst, num_fact, num_add, max_val):
    arg = [num_fact, num_add, max_val]
    for e in lst:
        if isinstance(e, float) or isinstance(e, str):
            return "Error. Unexpected entries"
    for a in arg:
        if isinstance(a, float) or isinstance(a, str) or a <= 0:
            return "Error. Unexpected entries"
    products = list(x for x in itertools.combinations(lst, num_fact))
    sums = list(functools.reduce(lambda x, y: x * y, q) for q in products)
    united_sums_tuple = list(x for x in itertools.combinations(sums, num_add))
    united_sums = list(sum(s) for s in united_sums_tuple)
    below = equal = higher = 0
    for i in united_sums:
        if i < max_val:
            below += 1
        elif i == max_val:
            equal += 1
        else:
            higher += 1
    if num_fact > len(lst):
        return "Error. Number of factors too high"
    elif num_add > len(products):
        return "Error. Number of addens too high"
    else:
        return [{f"Below than {max_val}": below},
                {f"Equals to {max_val}": equal},
                {f"Higher than {max_val}": higher}]


lst_1 = [2, 10, 20, 15]
num_fact_1 = 3
num_add_1 = 2
max_val_1 = 701
print(eval_prod_sum(lst_1, num_fact_1, num_add_1, max_val_1))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# from itertools import combinations
# from math import comb, prod
#
# def eval_prod_sum(numbers: list, factor_count: int, addend_count: int, max_value: int) -> list or str:
#     if not (all(isinstance(i, int) for i in numbers) and
#             all(isinstance(i, int) and i > 0 for i in {factor_count, addend_count, max_value})):
#         return 'Error. Unexpected entries'
#     if factor_count > len(numbers):                     return 'Error. Number of factors too high'
#     if addend_count > comb(len(numbers), factor_count): return 'Error. Number of addens too high'
#
#     lower = equal = higher = 0
#     for sum_ in map(sum, combinations(map(prod, combinations(numbers, r=factor_count)), r=addend_count)):
#         if   sum_ < max_value: lower  += 1
#         elif sum_ > max_value: higher += 1
#         else:                  equal  += 1
#     return [{f'Below than {max_value}': lower}, {f'Equals to {max_value}': equal},
#             {f'Higher than {max_value}': higher}]
