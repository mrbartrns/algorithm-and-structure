# BOJ 1063
import sys

si = sys.stdin.readline

directions = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1),
              'LB': (-1, -1)}
king, stone, n = si().split()
kx, ky = ord(king[0]) - ord('A'), int(king[1]) - 1
sx, sy = ord(stone[0]) - ord('A'), int(stone[1]) - 1
for _ in range(int(n)):
    op = si().strip()
    dx, dy = directions[op]
    nkx = kx + dx
    nky = ky + dy
    nsx = sx + dx
    nsy = sy + dy
    if nkx < 0 or nkx >= 8 or nky < 0 or nky >= 8:
        continue
    if nkx == sx and nky == sy:
        if nsx < 0 or nsx >= 8 or nsy < 0 or nsy >= 8:
            continue
        sx, sy = nsx, nsy
    kx, ky = nkx, nky

king_location = chr(kx + ord('A')) + str(ky + 1)
stone_location = chr(sx + ord('A')) + str(sy + 1)
print(king_location)
print(stone_location)
