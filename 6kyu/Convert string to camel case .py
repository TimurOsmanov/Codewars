# def to_camel_case(text):
#     text = text.replace('-', '_')
#     first_word, *other = text.split('_')
#     answer = ''
#     for word in other:
#         i = 0
#         for letter in word:
#             if i == 0:
#                 letter = letter.upper()
#                 i += 1
#                 answer += letter
#             else:
#                 answer += letter
#     return first_word + answer

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')