t = int(input())
for u in range(t):
    n = int(input())
    arr = []
    issue = []
    flag = 0
    x = 0
    y = 0

    for _ in range(n):
        temp_arr = []
        string = input()
        for c in string:
            temp_arr.append(int(c))
        arr.append(temp_arr)
        
    for i in range(len(arr)):
        if 2 in arr[i]:
            x = i
    for j in range(len(arr[x])):
        if arr[x][j] == 2:
            y = j

    for i in range(len(arr)):
        temp = []
        for j in range(len(arr[0])):
            temp.append(True) if arr[i][j] == 1 else temp.append(False)
        issue.append(temp)
    
    def maze(arr, x, y):
        global issue, flag
        if arr[x][y] == 3:
            # print('현위치:', x, y)
            flag = 1
            return
        elif x < 0 or x >= len(arr) or y < 0 or y >= len(arr[0]):
            return
        else:
            
            if not issue[x][y]:
                issue[x][y] = True
                
                if y - 1 >= 0 and arr[x][y - 1] != 1:
                    print('현위치:', x, y)
                    maze(arr, x, y - 1)
                if x - 1 >= 0 and arr[x - 1][y] != 1:
                    print('현위치:', x, y)
                    maze(arr, x - 1, y)
                if y + 1 < len(arr) and arr[x][y + 1] != 1:
                    print('현위치:', x, y)
                    maze(arr, x, y + 1)
                if x + 1 < len(arr) and arr[x + 1][y] != 1:
                    print('현위치:', x, y)
                    maze(arr, x + 1, y)
                issue[x][y] = False

    maze(arr, x, y)
    print(f'#{u + 1} {flag}')
