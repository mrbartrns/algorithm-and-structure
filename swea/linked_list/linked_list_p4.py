def get_seq(arr, iter, index):
    for _ in range(iter):
        command = [x for x in input().split()]
        if command[0] == "I":
            arr[int(command[1]) : int(command[1])] = [int(command[2])]
        elif command[0] == "D":
            copy = arr[: int(command[1])] + arr[int(command[1]) + 1 :]
            arr = copy
        elif command[0] == "C":
            arr[int(command[1])] = int(command[2])
    if index >= len(arr):
        return -1
    return arr[index]


t = int(input())
for tc in range(t):
    n, m, l = map(int, input().split())
    seq = [int(x) for x in input().split()]
    print(f"#{tc + 1} {get_seq(seq, m, l)}")
