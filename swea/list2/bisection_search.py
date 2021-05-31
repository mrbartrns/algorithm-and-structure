def bisection_search(arr: list, n: int) -> bool:
    mid = len(arr) // 2
    if len(arr) < 2:
        if arr[mid] == n:
            return True
        else:
            return False
    else:
        if arr[mid] == n:
            return True
        else:
            return bisection_search(arr[:mid], n) if arr[mid] > n else bisection_search(arr[mid:], n)

print(bisection_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 11], 12))
