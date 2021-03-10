# SWEA 2056
days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = int(input())
for tc in range(t):
    date = input().strip()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if days[int(month)] >= int(day):
        ans = year + "/" + month + "/" + day
    else:
        ans = str(-1)
    print("#" + str(tc + 1), ans)