def find_string(t, p):
    n = len(t)
    m = len(p)
    begin = 0
    matched = 0
    f = failure_function(p)
    while begin <= n - m:
        if t[begin + matched] == p[matched]:
            matched += 1
            if matched == m:
                return 1
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - f[matched - 1]
                matched = f[matched - 1]
    return 0

def failure_function(p):
    begin = 1
    m = len(p)
    matched = 0
    f = [0 for _ in range(m)]

    while begin + matched < m:
        if p[begin + matched] == p[matched]:
            matched += 1
            f[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - f[matched - 1]
                matched = f[matched - 1]
    return f

t = int(input())
for i in range(t):
    p = input()
    t = input()
    print(f'#{i + 1} {find_string(t, p)}')

# print(find_string('EOGGXYPVSY', 'XYPV'))
# print(find_string('HOFSTJPVPP','STJJ'))
# print(find_string('TTXGZYJZXZTIBSDGWQLW','ZYJZXZTIBSDG'))