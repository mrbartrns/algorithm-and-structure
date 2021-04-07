# BOJ 20055
import sys
from collections import deque

si = sys.stdin.readline

# 컨베이어 벨트의 시작점과 끝점만 바꿔주는 형식
n, k = map(int, si().split())
belt = deque(list(map(int, si().split())))
answer = 1

# robot이 들어온 순서대로 자신의 위치를 담고 있기
robot = deque([0] * 2 * n)
while True:
    # step 1
    belt.rotate(1)
    robot.rotate(1)
    robot[n - 1] = 0

    # step 2: 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면, 이동
    # 거꾸로 탐색
    for i in range(n - 2, -1, -1):
        if robot[i] != 0 and robot[i + 1] == 0 and belt[i + 1] >= 1:
            belt[i + 1] -= 1
            robot[i + 1] = robot[i]
            robot[i] = 0
    robot[n - 1] = 0

    # step 3
    if robot[0] == 0 and belt[0] > 0:
        belt[0] -= 1
        robot[0] = 1

    # step 4
    cnt = 0
    for i in range(len(belt)):
        if belt[i] == 0:
            cnt += 1
    if cnt >= k:
        print(answer)
        break
    answer += 1
