# BOJ 1373
import sys

input = sys.stdin.readline

num = input().strip()
# num = "1" * 100000
sys.stdout.write(oct(int(num, 2))[2:])