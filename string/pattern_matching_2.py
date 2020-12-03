def bfs(t, p):
    n = len(t)
    m = len(p)
    begin = 0 # t counter
    matched = 0 # p counter
    while  begin <= n - m:
        if t[begin + matched] == p[matched]:
            matched += 1
            if matched == m:
                return begin
        else:
            begin += 1
            matched = 0
    return -1

def bfs2(t, p):
    n = len(t)
    m = len(p)
    i = 0
    j = 0
    while i <= n - m:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == m:
            return i - m
        else:
            return -1

# kmp는 실패했을 때 몇칸을 띌 것인지에 대해서 생각하는 알고리즘
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
                begin = matched - f[matched - 1]
                matched = f[matched - 1]
    return res

def failure_function(p):
    m = len(p)
    begin = 1
    matched = 0
    f = [0 for _ in range(m)]
    while begin + matched < m:
        if p[begin + matched] == p[matched]:
            matched += 1
            f[begin + matched - 1] = 1
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - f[matched - 1]
                matched = f[matched - 1]
    return f

def bm(t, p):
    n = len(t)
    m = len(p)
    i = m - 1
    j = m - 1
    skip_table = skip(p)
    while j >= 0:
        while t[i] != p[j]:
            k = skip_table[ord(t[i])]
            # if m - j > k:
            #     i += m - j
            # else:
            #     i += k
            i += k
            if i >= n:
                return -1
        j = m - 1
        i -= 1
        j -= 1
    return i + 1

def skip(p):
    m = len(p)
    ALPHABET_LENGTH = 25
    skip_table = [m for i in range(ALPHABET_LENGTH)]
    for i in range(m):
        skip_table[ord(p[i]) - ord('a')] = m - 1 - i
    return skip_table

print(bfs('abccabac', 'abac'))