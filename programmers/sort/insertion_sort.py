# 삽입 정렬은 최선의 경우 O(n)의 시간 복잡도를 가진다.
# 최악의 경우 O(n^2)이지만, O(n^2) 정렬 알고리즘 중 가장 빠른 편이다.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            # 현재 위치의 값이 바로 이전 위치보다 작다면,
            # j번째와 j - 1번째 값을 스왑한다.
            # 0번 인덱스까지 반복하고, 더 이상 j번째가 j - 1번째보다 작지 않다면 멈춘다.
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
insertion_sort(arr)
