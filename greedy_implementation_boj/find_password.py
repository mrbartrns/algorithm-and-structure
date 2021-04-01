# BOJ 17219
import sys

si = sys.stdin.readline
n, m = map(int, si().split())
passwords = {}
for _ in range(n):
    url, password = si().split()
    passwords[url] = password

for _ in range(m):
    url = si().strip()
    sys.stdout.write(passwords[url])
    print()
