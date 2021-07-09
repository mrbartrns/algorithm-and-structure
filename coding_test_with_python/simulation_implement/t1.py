# BOJ 18406 (럭키 스트레이트)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

string = si().strip()
mid = len(string) // 2
left = string[:mid]
right = string[mid:]
left_s = 0
right_s = 0
for i in range(mid):
    left_s += int(left[i])
    right_s += int(right[i])
print("LUCKY" if left_s == right_s else "READY")
