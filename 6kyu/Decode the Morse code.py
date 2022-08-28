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


# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' '))
#     for word in morseCode.strip().split('   '))
print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   '
                   '..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   '
                   '.-.. .- --.. -.--   -.. --- --. .-.-.-  '))
