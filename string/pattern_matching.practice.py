def kmp(t, p):
    n = len(t)
    m = len(p)
    begin = 0
    matched = 0
    res = []

    f = failure_function(p)

    while begin <= n - m:
        if matched < m and t[begin + matched] == p[matched]:
            matched += 1
            if matched == m:
                res.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                # begin 초기화 및 matched 초기화
                begin += (matched + f[matched - 1])
                matched = f[matched - 1]
    return res

def failure_function(p):
    m = len(p)
    
    begin = 1
    matched = 0
    
    f = [0 for i in range(m)]

    while begin + matched < m:
        if p[begin + matched] == p[matched]:
            matched += 1
            f.append(matched)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - f[matched - 1]
                matched = f[matched - 1]
    return f


print(kmp('abaabababc', 'ababab'))