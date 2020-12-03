# string pattern matching algorithm
'''
    1. BFS - 매칭 검색중 다른 문자가 나오면 패턴을 순회하는 반복을 멈추고 다시 패턴의 처음부터 비교 (인덱스 1을 증가시켜서)
    2. KMP
    3. BOYER-MOORE
'''

# bfs pattern matching
def bfs_matching(p, t): # p: pattern, t: target
    i = 0 # index of t
    j = 0 # index of p
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i -= j
            print('i:', i)
            j = -1
            print('j:', j)
        i += 1
        j += 1
        print('i:', i)
        print('j:', j)
    if j == len(p):
        return i - len(p)
    else:
        return -1

def failure_function(p):
    m = len(p)
    pi = [0 for i in range(m)]
    begin = 1
    matched = 0
    while begin + matched < m:
        if p[begin + matched] == p[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else: 
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

def kmp(t, p):
    n = len(t)
    m = len(p)
    ret = []
    pi = failure_function(p)
    begin = 0
    matched = 0
    while begin <= n - m:
        if matched < m and t[begin + matched] == p[matched]:
            matched += 1
            if matched == m:
                ret.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return ret

print(kmp('abaabababc', 'ababab'))