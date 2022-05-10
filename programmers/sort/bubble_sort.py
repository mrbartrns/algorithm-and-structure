# 버블 정렬
"""
오름차순 기준
인접한 두 요소를 비교하여 앞 요소가 뒤 요소보다 클 경우
서로 위치를 맞바꿈
가장 큰 요소부터 가장 뒤에 배치되기 시작하여 버블 정렬이라고 부름
"""


def bubble_sort(arr: list[int | float]):
    length = len(arr)

    for i in range(length):
        flag = True
        # 가장 뒤는 이미 정렬이 되어 있는 상태이므로 다시 확인할 필요가 없다.
        for j in range(length - i):
            if j + 1 >= length:
                continue
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        print(arr)
        if flag:
            break
