# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
# Ignore numbers and punctuation.
def is_pangram(s):
    s = s.lower()
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_dict = {x: 0 for x in alp}
    for letter in s:
        if letter in alp_dict:
            alp_dict[letter] += 1
    print(alp_dict)
    print(alp_dict.values())
    if any(x == 0 for x in alp_dict.values()):
        return False
    else:
        return True

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# import string
# def is_pangram(s):
#     return set(string.ascii_lowercase) <= set(s.lower())