# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b keeping their order.
# If a value is present in b, all of its occurrences must be removed from the other
def array_diff(a, b):
    ans = set(a) - set(b)
    b = []
    for x in a:
        if x in ans:
            b.append(x)
    return b


print(array_diff([1, 2, 2], [2]))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# def array_diff(a, b):
#     return [x for x in a if x not in b]
#
#
# print(array_diff([1,2,2],[2]))
