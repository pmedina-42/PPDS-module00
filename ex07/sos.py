import sys


morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}


def translate_to_morse(text):
    morse_code = []
    for char in text:
        if char.upper() in morse_dict:
            morse_code.append(morse_dict[char.upper()])
    return ' '.join(morse_code)


def main():
    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
        assert sys.argv[1].isalpha, "bad argument"
        morse_code = translate_to_morse(sys.argv[1])
        print(morse_code)
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == '__main__':
    main()