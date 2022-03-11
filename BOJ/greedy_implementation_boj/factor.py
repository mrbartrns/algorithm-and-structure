import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

while True:
    a, b = map(int, si().strip().split(" "))
    if a == 0 and b == 0:
        break
    switched = False
    if a < b:
        a, b = b, a
        switched = True
    if a % b == 0:
        if switched:
            print("factor")
        else:
            print("multiple")
    else:
        print("neither")
