import sys

try:
    assert not len(sys.argv) > 2, "more than one argument is provided"
    assert not len(sys.argv) < 2, "one argument needed"
    assert sys.argv[1].isdigit(), "argument is not an integer"
    whatis = "even" if int(sys.argv[1]) % 2 == 0 else "odd"
    print(f"I'm {whatis}")
except AssertionError as ae:
    print(f"AssertionError: {ae}")