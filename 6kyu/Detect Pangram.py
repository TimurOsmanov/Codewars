# def is_pangram(s):
#     s = s.lower()
#     alp = 'abcdefghijklmnopqrstuvwxyz'
#     alp_dict = {x: 0 for x in alp}
#     for letter in s:
#         if letter in alp_dict:
#             alp_dict[letter] += 1
#     print(alp_dict)
#     print(alp_dict.values())
#     if any(x == 0 for x in alp_dict.values()):
#         return False
#     else:
#         return True
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())