if __name__ == '__main__':
    x, k = input().split()
    x = int(x)
    eq = input()

    print(eval(eq) == int(k))


