# BOJ 12813
import sys

si = sys.stdin.readline

a = list(si().strip())
b = list(si().strip())
a_and_b = []
a_or_b = []
a_xor_b = []
not_a = []
not_b = []
for i in range(len(a)):
    if a[i] == "1":
        not_a.append("0")
    else:
        not_a.append("1")
    if b[i] == "1":
        not_b.append("0")
    else:
        not_b.append("1")

    if a[i] == b[i] == "1":
        a_and_b.append("1")
        a_or_b.append("1")
        a_xor_b.append("0")
    elif a[i] == b[i] == "0":
        a_and_b.append("0")
        a_or_b.append("0")
        a_xor_b.append("0")
    elif a[i] != b[i]:
        a_and_b.append("0")
        a_or_b.append("1")
        a_xor_b.append("1")

print("".join(a_and_b))
print("".join(a_or_b))
print("".join(a_xor_b))
print("".join(not_a))
print("".join(not_b))
