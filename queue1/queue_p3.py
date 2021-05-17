# 피자 만들기
# 1. 피자를 오븐에 넣는다.
# 2. 피자를 오븐에 다 넣었으면, 첫번째 피자부터 꺼내보면서 남은 치즈가 0이 되었는지 확인한다.
# 3. 0이되었다면, 그 자리에 있는 피자를 꺼내고 다른 피자를 넣는다.


def cook_pizza(arr: list, n: int) -> int:
    """
    arr: pizza 치즈의 양
    n: 오븐 칸 수
    queue: list(queue), oven
    pizzas: queue를 그대로 복사한 리스트
    in_oven: queue 안에 들어있는 피자의 갯수
    y: arr를 순환하기위한 iterator
    idx: queue의 idx
    counts: 다 구워진 피자의 갯수
    """
    queue = [-1] * n
    pizzas = [-1] * n
    in_oven = 0
    i = 0
    idx = 0
    counts = 0
    is_zero = False
    while counts < len(arr):
        j = idx
        while in_oven < len(queue) and i < len(arr):
            queue[j] = arr[i] // 2
            pizzas[j] = arr[i]
            i += 1
            in_oven += 1
            j = (j + 1) % len(queue)
        is_zero = False
        while not is_zero:
            # 여기서 무한 루프가 남
            if queue[j] != 0:
                queue[j] //= 2
                j = (j + 1) % len(queue)
            else:
                idx = j
                counts += 1
                in_oven -= 1
                queue[idx] = -1
                is_zero = True
    # print(pizzas[idx])
    for k in range(len(arr)):
        if arr[len(arr) - k - 1] == pizzas[idx]:
            return len(arr) - k


# print(cook_pizza([7, 2, 6, 5, 3], 3))
# print(cook_pizza([5, 9, 3, 9, 9, 2, 5, 8, 7, 1], 5))
# print(cook_pizza([20, 4, 5, 7, 3, 15, 2, 1, 2, 2], 5))

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    print(f"#{i + 1} {cook_pizza(arr, n)}")
