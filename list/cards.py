def get_biggest_cards(arr):
    idx = 0
    many = 0
    counts = [0] * 10
    for i in arr:
        counts[i] += 1
  
    for i in range(len(counts)):
        if many <= counts[i]:
            many = counts[i]
            idx = i
    return [idx, many]

# print(get_biggest_cards([4, 4, 6, 9, 9]))

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    arr =[int(i) for i in s]
    res = get_biggest_cards(arr)
    print(f'#{i + 1} {res[0]} {res[1]}')
