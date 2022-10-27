# Complete the function/method (depending on the language) to return true/True when its argument is an array
# that has the same nesting structures and same corresponding length of nested arrays as the first array.
# should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
#
# should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
#
# should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
#
# should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
original_seq, other_seq = [], []


def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        def decompose(array, array_len):
            for x in array:
                if isinstance(x, list):
                    array_len.append(len(x))
                    decompose(x, array_len)
                else:
                    array_len.append(1)
            return array_len

        return decompose(original, []) == decompose(other, [])
    return False


print(same_structure_as([1, '[', ']'], ['[', ']', 1]))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# def same_structure_as(original,other):
#     if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
#         for o1, o2 in zip(original, other):
#             if not same_structure_as(o1, o2): return False
#         else: return True
#     else: return not isinstance(original, list) and not isinstance(other, list)
