if __name__ == '__main__':
    N = int(input())
    commandList = []
    l = []
    for i in range(N):
        commandList.append(input().split())

    for e in commandList:
        command = e[0]
        if command == "insert":
            l.insert(int(e[1]), int(e[2]))
        elif command == "print":
            print(l)
        elif command == "remove":
            l.remove(int(e[1]))
        elif command == "append":
            l.append(int(e[1]))
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop()
        elif command == "reverse":
            l.reverse()

