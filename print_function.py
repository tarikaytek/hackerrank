if __name__ == '__main__':
    n = int(input())


def f(x):
    print(*range(1, x + 1), sep="")


f(n)