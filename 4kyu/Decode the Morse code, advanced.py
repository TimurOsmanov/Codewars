ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    'SOS': '...---...', '!': '-.-.--', '.': '.-.-.-'}

MORSE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_MORSE.items()}


def decode_bits(bits):
    bits = str(bits).rstrip('0').strip('0')
    symb, *other = str(bits).split('0')
    n = len(symb)
    m = n // 3
    bits_dot = str(bits).replace('0' * 7 * n, '   ').replace('1' * 3 * n, '-') \
        .replace('0' * 3 * n, ' ').replace('0' * n, '').replace('1' * n, '.')
    bits_dash = str(bits).replace('0' * 7 * m, '   ').replace('1' * 3 * m, '-') \
        .replace('0' * 3 * m, ' ').replace('0' * m, '').replace('1' * m, '.')
    try:
        decode_morse(bits_dot)
        return bits_dot
    except KeyError:
        return bits_dash


def decode_morse(morse_code):
    return ' '.join(map(
        lambda x: ''.join(map(
            lambda z: MORSE_TO_ENGLISH[z],
            x.strip().split())),
        morse_code.strip().split('   ')))

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# def decodeBits(bits):
#     import re
#
#     # remove trailing and leading 0's
#     bits = bits.strip('0')
#
#     # find the least amount of occurrences of either a 0 or 1, and that is the time hop
#     time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
#
#     # hop through the bits and translate to morse
#     return bits[::time_unit].replace('111', '-').replace('1', '.').\
#         replace('0000000', '   ').replace('000', ' ').replace('0', '')
#
#
# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))



print(decode_morse(decode_bits('000000011100000')))
