import sys

try:
    assert not len(sys.argv) > 2, "more than one argument is provided"
    assert not len(sys.argv) < 2, "one argument needed"
    try:
        num = int(sys.argv[1])
    except:
        raise AssertionError("argument is not an integer")
    whatis = "even" if num % 2 == 0 else "odd"
    print(f"I'm {whatis}")
except AssertionError as ae:
    print(f"AssertionError: {ae}")
