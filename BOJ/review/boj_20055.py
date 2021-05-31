# BOJ 20055 (컨베이어 벨트 위의 로봇)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, k = map(int, si().split())
belt = deque(list(map(int, si().split())))
robot = deque([0] * 2 * n)
step = 1
while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[n - 1] = 0

    for i in range(n - 2, -1, -1):
        if robot[i] != 0 and robot[i + 1] == 0 and belt[i + 1] > 0:
            belt[i + 1] -= 1
            robot[i + 1] = robot[i]
            robot[i] = 0
    robot[n - 1] = 0

    if belt[0] > 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1

    cnt = 0
    for i in range(2 * n):
        if belt[i] == 0:
            cnt += 1

    if cnt >= k:
        break
    step += 1

print(step)
