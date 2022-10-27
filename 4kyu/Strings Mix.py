# Given two strings s1 and s2, we want to visualize how different the two strings are.
# We will only take into account the lowercase letters (a to z).
# First let us count the frequency of each lowercase letters in s1 and s2.
#
# s1 = "A aaaa bb c"
#
# s2 = "& aaa bbb c d"
#
# s1 has 4 'a', 2 'b', 1 'c'
#
# s2 has 3 'a', 3 'b', 1 'c', 1 'd'
#
# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2.
# In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.
#
# We can resume the differences between s1 and s2 in the following string:
# "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4.
# In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.
#
# The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum
# if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string
# where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.
#
# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix)
# will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order
# (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'.
# See examples and "Example Tests".
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

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
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
