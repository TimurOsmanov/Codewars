# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
x = [1, 0, 1, 2, 0, 1, 3]


def move_zeros(array):
    new_array = [t for t in array if t != 0]
    while len(new_array) != len(array):
        new_array.append(0)
    return new_array


print(move_zeros(x))
# def move_zeros(array):
#     return sorted(array, key=lambda x: x==0 and type(x) is not bool)

# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))
