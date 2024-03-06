import sys


def main():
    """tu puta madre"""
    upper = lower = punct = digits = spaces = 0
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            s = ""
            while True:
                char = sys.stdin.read(1)
                if char == '\n':
                    s += ' '
                elif char == '':
                    spaces += 1
                    break
                else:
                    s += char
        else:
            assert len(sys.argv) == 2, "more than one argument provided"
            s = sys.argv[1]
        assert isinstance(s, (str, int)), "provide a string"
        
        for c in s:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c.isdigit():
                digits += 1
            elif c in punctuation:
                punct += 1
            elif c.isspace() or c == '\n':
                spaces += 1
        
        print(f"The text contains {len(s)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except AssertionError as ae:
        print(f"{type(ae).__name__}: {ae}")
    except KeyboardInterrupt as ki:
        print(f"{type(ki).__name__}: Ctrl+C pressed")
    except EOFError as eof:
        print(f"{type(eof).__name__}: Ctrl+D pressed")


if __name__ == "__main__":
    main()
