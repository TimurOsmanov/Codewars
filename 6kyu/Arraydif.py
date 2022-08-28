# def array_diff(a, b):
#     ans = set(a) - set(b)
#     b = []
#     for x in a:
#         if x in ans:
#             b.append(x)
#     return b


def array_diff(a, b):
    return [x for x in a if x not in b]


print(array_diff([1,2,2],[2]))
