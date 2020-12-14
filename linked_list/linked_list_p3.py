def print_reverse(arr, n):
    string = ""
    i = 0
    length = len(arr)
    number = n if length > n else length
    while i < number:
        string += str(arr[length - i - 1])
        if i != length - 1:
            string += " "
        i += 1
    return string


t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())
    linked_list = [int(x) for x in input().split()]
    idx = 0
    i = 0
    while i < k:
        idx = (idx + m) % (len(linked_list))
        if idx % len(linked_list) == 0:
            length = len(linked_list)
            linked_list[length:length] = [linked_list[idx] + linked_list[idx - 1]]
            idx = len(linked_list) - 1
        else:
            linked_list[idx:idx] = [linked_list[idx] + linked_list[idx - 1]]
        i += 1
    print(f"#{tc + 1} {print_reverse(linked_list, 10)}")

"""
n, m, k = 5, 3, 5
linked_list = [958, 386, 329, 169, 778]
# n, m, k = 6, 3, 3
# linked_list = [6, 2, 4, 9, 1, 5]
i = 0
idx = 0
while i < k:
    idx = (idx + m) % (len(linked_list))
    if idx % len(linked_list) == 0:
        length = len(linked_list)
        linked_list[length:length] = [linked_list[idx] + linked_list[idx - 1]]
        idx = len(linked_list) - 1
    else:
        linked_list[idx:idx] = [linked_list[idx] + linked_list[idx - 1]]
    i += 1
print(print_reverse(linked_list, 10))
"""
