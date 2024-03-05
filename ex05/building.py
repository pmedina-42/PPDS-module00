import sys


def main():
    """tu puta madre"""
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    try:
        if (len(sys.argv) == 1):
            s = input('What is the text to count?\n')
        assert not len(sys.argv) > 2, "more than one argument provided"
        if (len(sys.argv) == 2):
            s = sys.argv[1]
        assert type(s) is str or type(s) is int, "provide a string"
        upper = lower = punct = digits = spaces = 0
        for c in s:
            if (c.isupper()):
                upper += 1
            elif (c.islower()):
                lower += 1
            elif (c.isdigit()):
                digits += 1
            elif (c.isspace()):
                spaces += 1
            elif (c in punctuation):
                punct += 1
        print(f"The text contains {str(len(s))} characters:")
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
