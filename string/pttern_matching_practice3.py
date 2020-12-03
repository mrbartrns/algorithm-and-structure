def counts(p):
    a_dict = {}
    for i in range(len(p)):
        if p[i] not in a_dict.keys():
            a_dict[p[i]] = 0
    return a_dict

def solve(t, p):
    a_dict = counts(p)
    for i in range(len(t)):
        if t[i] in a_dict:
            a_dict[t[i]] += 1
    
    res = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    return res[0][1]

t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    print(f'#{i + 1} {solve(str2, str1)}')