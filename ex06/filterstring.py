import sys
from ft_filter import ft_filter


def checker():
    pt = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    assert not len(sys.argv) != 3, "the correct number of arguments is 2"
    assert sys.argv[2].isdigit, "second argument is not an integer"
    assert sys.argv[1] not in pt and sys.argv[1].isprintable, "forbidden chars"


def main():
    try:
        checker()
        lst = sys.argv[1].split()
        num = int(sys.argv[2])
        res = ft_filter(lambda x: len(x) >= num, lst)
        print(res)

    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == "__main__":
    main()
