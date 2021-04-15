
    

n = 14
k = 0

counts = 0
iss1 = [False] * n
iss2 = [False] * (2 * n - 1)
iss3 = [False] * (2 * n - 1)
ans = []

def solve_n_queen(k, n):
    global counts, iss1, iss2, iss3
    if k == n:
        counts += 1
        return

    else:
        for j in range(n):
            # if (not iss1[x]) and (not iss2[k + x]) and (not iss3[k - x + n - 1]):
            if iss1[j] or iss2[k + j] or iss3[k - j + n - 1]:
                continue
            iss1[j], iss2[k + j], iss3[k - j + n - 1] = True, True, True
            solve_n_queen(k + 1, n)
            iss1[j], iss2[k + j], iss3[k - j + n - 1] = False, False, False

for i in range(1, 15):
    solve_n_queen(k, i)
    print(counts)
    ans.append(counts)
    counts = 0

print(ans)


