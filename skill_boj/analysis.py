# BOJ 10820


def solve(sentence):
    res = [0] * 4
    for i in range(len(sentence)):
        if ord(sentence[i]) >= ord("a") and ord(sentence[i]) <= ord("z"):
            res[0] += 1
        elif ord(sentence[i]) >= ord("A") and ord(sentence[i]) <= ord("Z"):
            res[1] += 1
        elif ord(sentence[i]) >= ord("0") and ord(sentence[i]) <= ord("9"):
            res[2] += 1
        elif sentence[i] == " ":
            res[3] += 1
    return " ".join(list(map(str, res)))


while True:
    try:
        sentence = input()
        print(solve(sentence))
    except EOFError:
        break