# BOJ 14470
import sys

si = sys.stdin.readline

init_temp = int(si())
target_temp = int(si())
f_time = int(si())
defrost_time = int(si())
n_time = int(si())
cur_temp = init_temp
time = 0
frozen = True
while True:
    if target_temp == cur_temp:
        print(time)
        break
    if cur_temp < 0:
        cur_temp += 1
        time += f_time
    elif frozen and cur_temp == 0:
        frozen = False
        time += defrost_time
    else:
        cur_temp += 1
        time += n_time
