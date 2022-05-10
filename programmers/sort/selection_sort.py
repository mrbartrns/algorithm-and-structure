# 선택 정렬의 경우 최악의 경우와 최선의 경우, 평균 모두 O(n**2)의 시간복잡도를 가진다.
def selection_sort(arr: list[int | float]):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
