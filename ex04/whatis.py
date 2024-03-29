import sys

try:
    assert not len(sys.argv) > 2, "more than one argument is provided"
    assert not len(sys.argv) < 2, "one argument needed"
    num = int(sys.argv[1])
    whatis = "even" if num % 2 == 0 else "odd"
    print(f"I'm {whatis}")
except AssertionError as ae:
    print(f"{type(ae).__name__}: {ae}")
except ValueError:
    print("AssertionError: argument is not an integer")
