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

# def sum_of_intervals(intervals):
#     result = set()
#     for start, stop in intervals:
#         for x in range(start, stop):
#             result.add(x)
#
#     return len(result)