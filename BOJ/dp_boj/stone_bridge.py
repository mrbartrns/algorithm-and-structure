# BOJ 2602 돌다리 건너기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def cross_bridge(t, idx, char_idx):
    if char_idx >= len(target_string):
        return 1
    if idx >= len(bridge[0]):
        return 0
    if cache[t][idx][char_idx] > -1:
        return cache[t][idx][char_idx]
    cache[t][idx][char_idx] = 0
    if bridge[t][idx] == target_string[char_idx]:
        cache[t][idx][char_idx] += cross_bridge(1 - t, idx + 1, char_idx + 1)
    cache[t][idx][char_idx] += cross_bridge(t, idx + 1, char_idx)
    return cache[t][idx][char_idx]


target_string = si().strip()
bridge = []
for _ in range(2):
    bridge.append(si().strip())
cache = [
    [[-1 for _ in range(len(target_string))] for _ in range(len(bridge[0]))]
    for _ in range(2)
]

answer = 0
answer += cross_bridge(0, 0, 0) + cross_bridge(1, 0, 0)
print(answer)
