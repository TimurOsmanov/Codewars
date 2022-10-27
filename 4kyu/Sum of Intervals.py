# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals,
# and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
#
# Intervals
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
#
# Overlapping Intervals
# List containing overlapping intervals
# Tests with large intervals
# Your algorithm should be able to handle large intervals.
# All tested intervals are subsets of the range [-1000000000, 1000000000].
def sum_of_intervals(intervals):
    sort_intervals = sorted(intervals)
    initial_set = set(range(sort_intervals[0][0], sort_intervals[0][1] + 1))
    new_intervals, answer = [], 0
    for it in sort_intervals:
        if initial_set & set(range(it[0], it[1] + 1)):
            initial_set |= set(range(it[0], it[1] + 1))
        else:
            new_intervals.append(list(sorted(initial_set)))
            initial_set = set(range(it[0], it[1] + 1))
    new_intervals.append(list(sorted(initial_set)))
    for interval in new_intervals:
        answer += (interval[-1] - interval[0])
    return answer


print(sum_of_intervals([(-479, 294),
                        (-338, -256),
                        (-70, 11),
                        (-53, 6),
                        (105, 138),
                        (123, 442),
                        (215, 402),
                        (341, 407),
                        (423, 444),
                        (457, 461),
                        (464, 482),
                        (470, 484),
                        (483, 489)]))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# def sum_of_intervals(intervals):
#     result = set()
#     for start, stop in intervals:
#         for x in range(start, stop):
#             result.add(x)
#
#     return len(result)
