h = eval(input("Enter row of Diamond : "))
i = int(input("Enter amount of diamond : "))
def diamond():
    for k in range(i):
        for x in range(h):
            print(" " * (h - x), "*" * (2*x + 1))
        for x in range(h - 2, -1, -1):
            print(" " * (h - x), "*" * (2*x + 1))
diamond()