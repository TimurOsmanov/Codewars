# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
def to_camel_case(text):
    text = text.replace('-', '_')
    first_word, *other = text.split('_')
    answer = ''
    for word in other:
        i = 0
        for letter in word:
            if i == 0:
                letter = letter.upper()
                i += 1
                answer += letter
            else:
                answer += letter
    return first_word + answer

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# def to_camel_case(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
