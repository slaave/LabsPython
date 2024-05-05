MORSE_CODE_DICT = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
                   'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
                   'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
                   'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
                   'Ю': '..--', 'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
                   ';': '-.-.-.', ':': '---...', '?': '..--..', '!': '-.-.--', '-': '-....-', ' ': '\t'}
MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def encode_morse(text):
    encoded_text = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            encoded_text += MORSE_CODE_DICT[char] + ' '
        else:
            encoded_text += char
    return encoded_text.strip()

def decode_morse(morse_text):
    decoded_text = ''
    print(MORSE_DICT)

    for char in morse_text.split(' '):
        if char in MORSE_DICT:
            decoded_text += MORSE_DICT[char]
        else:
            decoded_text += char
    return decoded_text
