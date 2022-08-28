def mix(s1, s2):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_dict = {x: 0 for x in alp}
    s1_letter_count, s2_letter_count = {}, {}
    answer = []
    answer_end = str()
    for letter in s1:
        if letter in alp_dict:
            if letter in s1_letter_count:
                s1_letter_count[letter] += 1
            else:
                s1_letter_count[letter] = 1
    for letter in s2:
        if letter in alp_dict:
            if letter in s2_letter_count:
                s2_letter_count[letter] += 1
            else:
                s2_letter_count[letter] = 1
    s1_new = {key: value for key, value in s1_letter_count.items() if value != 1}
    s2_new = {key: value for key, value in s2_letter_count.items() if value != 1}
    keys_ans = sorted(set(x for x in s1_new.keys()) | set(y for y in s2_new.keys()))
    for x in keys_ans:
        if x in s1_new and x in s2_new:
            if s1_new[x] > s2_new[x]:
                answer.append('1:' + str(x * s1_new[x]) + '/')
            elif s2_new[x] > s1_new[x]:
                answer.append('2:' + str(x * s2_new[x]) + '/')
            elif s2_new[x] == s1_new[x]:
                answer.append('3:' + str(x * s1_new[x]) + '/')
        elif x in s1_new and x not in s2_new:
            answer.append('1:' + str(x * s1_new[x]) + '/')
        elif x in s2_new and x not in s1_new:
            answer.append('2:' + str(x * s2_new[x]) + '/')
    for x in sorted(answer, key=lambda x: (len(x), -int(x[0])), reverse=True):
        answer_end += x
    return answer_end[:-1].replace('3', '=')


print(mix("looping is fun but dangerous", "less dangerous than coding"))
# def mix(s1, s2):
#     s = []
#     lett = "abcdefghijklmnopqrstuvwxyz"
#     for ch in lett:
#         val1, val2 = s1.count(ch), s2.count(ch)
#         if max(val1, val2) >= 2:
#             if val1 > val2:
#                 s.append("1:" + val1 * ch)
#             elif val1 < val2:
#                 s.append("2:" + val2 * ch)
#             else:
#                 s.append("=:" + val1 * ch)
#
#     s.sort()
#     s.sort(key=len, reverse=True)
#     return "/".join(s)
