# In this kata you have to deal with "real-life" scenarios, when Morse code transmission speed slightly varies
# throughout the message as it is sent by a non-perfect human operator. Also the sampling frequency may not be
# a multiple of the length of a typical "dot".
# For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may actually be received as follows:
#
# 0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000/
# 101100011111100000111110011101100000100000
#
# As you may see, this transmission is generally accurate according to the standard, but some dots and
# dashes and pauses are a bit shorter or a bit longer than the others.
#
# Note also, that, in contrast to the previous kata, the estimated average rate (bits per dot) may not be a
# whole number – as the hypotetical transmitter is a human and doesn't know anything about the receiving
# side sampling rate.
#
# For example, you may sample line 10 times per second (100ms per sample), while the operator transmits so
# that his dots and short pauses are 110-170ms long. Clearly 10 samples per second is enough resolution for
# this speed (meaning, each dot and pause is reflected in the output, nothing is missed), and dots would be
# reflected as 1 or 11, but if you try to estimate rate (bits per dot), it would not be 1 or 2, it would
# be about (110 + 170) / 2 / 100 = 1.4. Your algorithm should deal with situations like this well.
#
# Also, remember that each separate message is supposed to be possibly sent by a different operator,
# so its rate and other characteristics would be different. So you have to analyze each message (i. e. test)
# independently, without relying on previous messages. On the other hand, we assume the transmission
# charactestics remain consistent throghout the message, so you have to analyze the message as a whole to make
# decoding right. Consistency means that if in the beginning of a message '11111' is a dot and '111111' is a dash,
# then the same is true everywhere in that message. Moreover, it also means '00000' is definitely a short (in-character)
# pause, and '000000' is a long (between-characters) pause.
#
# That said, your task is to implement two functions:
#
# 1. Function decodeBitsAdvanced(bits), that should find an estimate for the transmission rate of the message,
# take care about slight speed variations that may occur in the message, correctly decode the message to dots .,
# dashes - and spaces (one between characters, three between words) and return those as a string.
# Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them.
# If message is empty or only contains 0's, return empty string. Also if you have trouble discerning
# if the particular sequence of 1's is a dot or a dash, assume it's a dot. If stuck, check this for ideas.
#
# 2. Function decodeMorse(morseCode), that would take the output of the previous function and return
# a human-readable string. If the input is empty string or only contains spaces, return empty string.
#
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.
#
# The Morse code table is preloaded for you as MORSE_CODE dictionary, feel free to use it. For C,
# the function morse_code acts like the dictionary. For C++, Scala and Go, a map is used. For C#,
# it's called Preloaded.MORSE_CODE. For Racket, a hash called MORSE-CODE is used.
#
# (hash-ref MORSE-CODE "".-.") ; returns "C"
# Of course, not all messages may be fully automatically decoded. But you may be sure that all
# the test strings would be valid to the point that they could be reliably decoded as described above,
# so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!
#
# Good luck!
import re

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    'SOS': '...---...', '!': '-.-.--', '.': '.-.-.-'}

MORSE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_MORSE.items()}


def decodeBitsAdvanced(bits):
    bits = bits.strip('0')
    time_units = sorted(set((len(m), m[0]) for m in re.findall(r"1+|0+", bits)))
    time_units_dict = {'0': [], '1': []}
    _ = [time_units_dict[x[1]].append(x[0]) for x in time_units if x[0] not in time_units_dict[x[1]]]
    dot_dash_list, pause_list = time_units_dict['1'][::-1], time_units_dict['0'][::-1]

    if len(dot_dash_list) <= 2 and len(pause_list) <= 3:
        if not dot_dash_list and not pause_list:
            return ''
        time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))

        if dot_dash_list and pause_list:
            dot_bit_pause = list(range(time_unit, time_unit * 3 - 1))[::-1]
            dash_char_pause = list(range(time_unit * 3 - 1, time_unit * 6 + 1))[::-1]
            max_ = max(len(m) for m in re.findall(r'1+|0+', bits)) if \
                max(len(m) for m in re.findall(r'1+|0+', bits)) > time_unit * 6 else time_unit * 6
            word_pause = list(range(time_unit * 6, max_ + 1))[::-1]

            bits = [bits := bits.replace('1' * dash, '-') for dash in dash_char_pause][-1]
            bits = [bits := bits.replace('1' * dot, '.') for dot in dot_bit_pause][-1]
            bits = [bits := bits.replace('0' * word, '   ') for word in word_pause][-1]
            bits = [bits := bits.replace('0' * character, ' ') for character in dash_char_pause][-1]
            bits = [bits := bits.replace('0' * bit, '') for bit in dot_bit_pause][-1]
            return bits

        return bits[::time_unit].replace('111', '-').replace('1', '.').\
            replace('0000000', '   ').replace('000', ' ').replace('0', '')

    dot_list, dash_list = clasterize(dot_dash_list)
    pause_list_new = pause_list[:pause_list.index(dot_list[0])]
    bit_pause = pause_list[pause_list.index(dot_list[0]):]
    char_pause, word_pause = clasterize(pause_list_new)

    bits = [bits := bits.replace('1' * dash, '-') for dash in dash_list][-1]
    bits = [bits := bits.replace('1' * dot, '.') for dot in dot_list][-1]
    bits = [bits := bits.replace('0' * word, '   ') for word in word_pause][-1]
    bits = [bits := bits.replace('0' * character, ' ') for character in char_pause][-1]
    bits = [bits := bits.replace('0' * bit, '') for bit in bit_pause][-1]
    return bits


def clasterize(bits_list):
    if not bits_list[1:-1]:
        return [bits_list[-1]], [bits_list[0]]
    for x in bits_list[1:-1]:
        init_a, init_b = bits_list[bits_list.index(x):], bits_list[:bits_list.index(x) + 1]
        st_dev_a = (sum([(x - (sum(init_a) / len(init_a)))**2 for x in init_a]) / len(init_a))**(1/2)
        st_dev_b = (sum([(x - (sum(init_b) / len(init_b)))**2 for x in init_b]) / len(init_b))**(1/2)
        if st_dev_a == st_dev_b:
            return init_a[1:], init_b
        if st_dev_a <= st_dev_b:
            return init_a, init_b[:-1]


def decodeMorse(morseCode):
    return ' '.join(map(
        lambda x: ''.join(map(
            lambda z: MORSE_TO_ENGLISH[z],
            x.strip().split())),
        morseCode.strip().split('   ')))


list_ = '00000000000000011111111000000011111111111100000000000111111111000001111111110100000000111111111111011000011111111011111111111000000000000000000011111111110000110001111111111111000111000000000001111111111110000111111111100001100111111111110000000000111111111111011100001110000000000000000001111111111010111111110110000000000000001111111111100001111111111110000100001111111111111100000000000111111111000000011000000111000000000000000000000000000011110001111100000111100000000111111111100111111111100111111111111100000000011110011111011111110000000000000000000000111111111110000000011111000000011111000000001111111111110000000001111100011111111000000000111111111110000011000000000111110000000111000000000011111111111111000111001111111111001111110000000000000000000001111000111111111100001111111111111100100000000001111111100111111110111111110000000011101111111000111000000001001111111000000001111111111000000000111100001111111000000000000011111111100111111110111111111100000000000111111110000001100000000000000000000111111101010000010000001111111100000000011111000111111111000000111111111110011111111001111111110000000011000111111110000111011111111111100001111100001111111100000000000011110011101110001000111111110000000001111000011111110010110001111111111000000000000000000111111111110000000100000000000000000011110111110000001000011101110000000000011111111100000011111111111100111111111111000111111111000001111111100000000000001110111111111111000000110011111111111101110001111111111100000000111100000111100000111111111100000111111111111000000011111111000000000001000000111100000001000001111100111111111110000000000000000000010001111111100000011111111100000000000000100001111111111110111001111111111100000111111100001111111111000000000000000000000000011100000111111111111011110000000010000000011111111100011111111111100001110000111111111111100000000000000111110000011111001111111100000000000011100011100000000000011111000001111111111101000000001110000000000000000000000000000111110010000000000111111111000011111111110000000000111111111111101111111111100000000010000000000000011111111100100001100000000000000111100111100000000001100000001111111111110000000011111111111000000000111100000000000000000000111101111111111111000000000001111000011111000011110000000001100111111100111000000000100111000000000000111110000010000011111000000000000001111111111100000000110111111111100000000000000111111111111100000111000000000111111110001111000000111111110111111000000001111000000000010000111111111000011110001111111110111110000111111111111000000000000000000000000111111111110000000111011111111100011111110000000001111111110000011111111100111111110000000001111111111100111111111110000000000110000000000000000001000011111111110000000001111111110000000000000000000000011111111111111000000111111111000001111111110000000000111111110000010000000011111111000011111001111111100000001110000000011110000000001011111111000011111011111111110011011111111111000000000000000000100011111111111101111111100000000000000001100000000000000000011110010111110000000011111111100000000001111100011111111111101100000000111110000011110000111111111111000000001111111111100001110111111111110111000000000011111111101111100011111111110000000000000000000000000010000111111111100000000001111111110111110000000000000000000000110000011110000000000001111111111100110001111111100000011100000000000111110000000011111111110000011111000001111000110000000011100000000000000111100001111111111100000111000000001111111111000000111111111100110000000001111000001111111100011100001111111110000010011111111110000000000000000000111100000011111000001111000000000111111001110000000011111111000100000000000011111111000011001111111100000000000110111000000000000111111111111000100000000111111111110000001111111111011100000000000000000000000000'
print(decodeMorse(decodeBitsAdvanced(list_)))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
# import re
#
# def decodeBitsAdvanced(bits):
#     out, bits = '', bits.strip('0')
#
#     if bits == "":
#         return bits
#
#     len1, len0 = map(len, re.findall(r'1+', bits)), map(len, re.findall(r'0+', bits))
#     mlen1 = min(len1)
#
#     mlen0 = min(len0) if len0 else mlen1
#     lenbit = max(len1) if max(len1) == min(mlen1, mlen0) else float(max(len1)) / 2
#
#     b = re.findall(r'1+|0+', bits)
#
#     for i in b:
#         if len(i) >= lenbit*2.3 and len(i) > 4 and i[0] == '0': out += '   '
#         elif len(i) > lenbit and i[0] == '1': out += '-'
#         elif len(i) > lenbit and i[0] == '0': out += ' '
#         elif len(i) <= lenbit and i[0] == '1': out += '.'
#
#     return out
#
#
# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_TO_ENGLISH[l] for l in w.split()) for w in morseCode.split('   '))
# list_ = '101'
# print(decodeMorse(decodeBitsAdvanced(list_)))
#
########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
# from itertools import groupby
#
#
# def decodeBitsAdvanced(bits):
#     bits = bits.strip("0")
#     if not bits: return ""
#
#     minall = min(len(list(g)) for b, g in groupby(bits))
#     maxone = max(len(list(g)) for b, g in groupby(bits) if b == "1")
#     dashlen = maxone if maxone != minall else minall * 3
#
#     normalized = "".join([
#         b * (1 if len(g) < (minall + dashlen) / 2.0
#         else 3 if len(g) <= dashlen + 2 else 7)
#         for b, g in ((b, list(g)) for b, g in groupby(bits))])
#
#     return (normalized.replace('0000000', '   ')
#                       .replace('111', '-')
#                       .replace('000', ' ')
#                       .replace('1', '.')
#                       .replace('0', ''))
#
#
# def decodeMorse(morse_code):
#     return " ".join(
#         "".join(MORSE_CODE.get(c, "%") for c in w.split(" "))
#         for w in morse_code.split("   ")) if morse_code else ""
# list_ = '101'
# print(decodeMorse(decodeBitsAdvanced(list_)))
#
