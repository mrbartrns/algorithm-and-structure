# BOJ 9656 돌게임2
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
print("SK" if N % 2 == 0 else "CY")
