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
for i in range(t):
    n, m = map(int, input().split())
    linked_list = [int(x) for x in input().split()]
    for _ in range(m - 1):
        temp = [int(x) for x in input().split()]
        check = True
        for j in range(len(linked_list)):
            if linked_list[j] > temp[0]:
                linked_list[j:j] = temp
                check = False
                break
        if check:
            linked_list.extend(temp)
    print(f"#{i + 1} {print_reverse(linked_list, 10)}")
    # print(linked_list)
