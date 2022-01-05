# BOJ 16500
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


string = si().strip()
N = int(si().strip())
words = []
for _ in range(N):
    words.append(si().strip())
cache = [0] * (len(string) + 1)
cache[0] = 1
for i in range(len(string)):
    prefix_length = i + 1
    for word in words:
        if prefix_length - len(word) < 0:
            continue
        if word == string[prefix_length - len(word) : prefix_length]:
            cache[prefix_length] = max(
                cache[prefix_length], cache[prefix_length - len(word)]
            )
print(cache[len(string)])
