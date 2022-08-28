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


def decode_morse(morse_code):
    return ' '.join(map(
        lambda x: ''.join(map(
            lambda z: MORSE_TO_ENGLISH[z],
            x.strip().split())),
        morse_code.strip().split('   ')))



def decode_bits(bits):
    bits = str(bits)
    dot, list_len, i, i1, i2 = bits[0], [], 1, 1, 0
    if dot == '0':
        pause = '1'
    else:
        pause = '0'
    for x in bits[1:]:
        if bits[i] == bits[i - 1]:
            i += 1
            i1 += 1
        else:
            list_len.append((bits[i - 1], i1))
            i1 = 1
            i += 1
    list_len.append((bits[i - i1], i1))
    n_pause = list_len[1][1]
    n_dot = list_len[2][1]
    m_pause = n_pause // 3
    m_dot = n_dot // 3
    bits_dot = str(bits).replace(pause * 7 * n_pause, '   ').replace(dot * 3 * n_dot, '-')\
        .replace(pause * 3 * n_pause, ' ').replace(pause * n_pause, '').replace(dot * n_dot, '.')
    bits_dash = str(bits).replace(pause * 7 * m_pause, '   ').replace(dot * 3 * m_dot, '-')\
        .replace(pause * 3 * m_pause, ' ').replace(pause * m_pause, '').replace(dot * m_dot, '.')
    print(bits_dash)
    try:
        decode_morse(bits_dot)
        return bits_dot
    except KeyError:
        return bits_dash


print(decode_morse(decode_bits('000000011100000')))