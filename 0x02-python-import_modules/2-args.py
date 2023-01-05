#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    k = len(sys.argv) - 1
    if k == 0:
        print("0 arguments.")
    elif k == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(k))
    for i in range(k):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
