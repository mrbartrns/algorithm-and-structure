# 퀵 정렬 알고리즘
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:  # 원소가 한개만 있을 경우
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:  # 엇갈렸으면 바로 종료
        # 피벗보다 큰 데이터를 찾을 때까지 반복실행
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복실행
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = (
                arr[pivot],
                arr[right],
            )  # 왼쪽의 값이 더 작으므로 (왼쪽값은 right)이다
        else:  # 엇갈리지 않았다면
            arr[right], arr[left] = arr[left], arr[right]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에 대해서 각각 실행


quick_sort(arr, 0, len(arr) - 1)
print(arr)