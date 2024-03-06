import sys


def translate_to_morse(text):
    """traduceme a tu puta madre"""
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    morse_code = []
    for char in text:
        if char.upper() in morse_dict:
            morse_code.append(morse_dict[char.upper()])
        else:
            raise AssertionError("character not in dictionary")
    return ' '.join(morse_code)


def main():
    """main otra vez de tu puta madre"""
    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
        assert sys.argv[1].isalpha, "bad argument"
        morse_code = translate_to_morse(sys.argv[1])
        print(morse_code)
    except AssertionError as ae:
        print(f"{type(ae).__name__}: {ae}")


if __name__ == '__main__':
    """main de tu puta madre"""
    main()
