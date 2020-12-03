import string
ALPAHBET_LENGTH = len(string.ascii_lowercase)

def skip(p):
    m = len(p)
    skip = [m for _ in range(ALPAHBET_LENGTH)]
    for i in range(m):
        skip[ord(p[i]) - ord('a')] = m - i - 1
    return skip

def boyer_moore(t, p):
    n = len(t)
    m = len(p)
    skip_table = skip(p)
    print(skip_table)
    i = m - 1
    j = m - 1

    while j >= 0:
        while t[i] != p[j]:
            k = skip_table[ord(t[i]) - ord('a')]

            if m - j > k:
                i += m - j
            else:
                i += k
            if i >= n:
                return n
            j = m - 1
        i -= 1
        j -= 1
    return i + 1

print(boyer_moore('abcxdezcacacabac', 'abac'))