#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    files = open(file, 'r')
    a = list(map(lambda x: int(x), files.read().splitlines()))
    for a in a:
        for i in range(1, a):
            if a % i == 0:
                if i > 1:
                    print("{:d} = {:d} * {:d}".format(a, (a // i), i))
                    break
