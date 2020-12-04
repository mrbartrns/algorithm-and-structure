def find_minimum_count(maze: list, issued: list, minimum_counts: list, zeros: list, x: int, y: int) -> None:
    if maze[x][y] == 3:
        if minimum_counts[0] == 0 or minimum_counts[0] >= len(zeros):
            minimum_counts[0] = len(zeros)
        return
    elif x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return
    else:
        if not issued[x][y]:
            issued[x][y] = True
            if maze[x][y] == 0:
                zeros.append(maze[x][y])
            if y - 1 >= 0 and maze[x][y - 1] != 1:
                find_minimum_count(maze, issued, minimum_counts, zeros, x, y - 1)
            if x - 1 >= 0 and maze[x - 1][y] != 1:
                find_minimum_count(maze, issued, minimum_counts, zeros, x - 1, y)
            if y + 1 < len(maze) and maze[x][y + 1] != 1:
                find_minimum_count(maze, issued, minimum_counts, zeros, x, y + 1)
            # x + 1이 5보다 크면 if문 자체가 에러가 난다.
            if x + 1 < len(maze) and maze[x + 1][y] != 1:
                find_minimum_count(maze, issued, minimum_counts, zeros, x + 1, y)
            if maze[x][y] == 0:
                zeros.pop()
            issued[x][y] = False

# maze = [
#     [1, 3, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 2, 1]
# ]

# zeros = []

# issued = []
# for i in range(len(maze)):
#     temp = []
#     for j in range(len(maze[0])):
#         temp.append(True) if maze[i][j] == 1 else temp.append(False)
#     issued.append(temp)

# # print(issued)
# minimum_counts = [0]
# x = 4
# y = 3

# find_minimum_count(maze, issued, minimum_counts, zeros, x, y)
# print(minimum_counts[0])

t = int(input())
for i in range(t):
    n = int(input())
    maze = []
    issued = []
    zeros = []
    minimum_counts = [0]

    for _ in range(n):
        temp_arr = []
        string = input()
        for c in string:
            temp_arr.append(int(c))
        maze.append(temp_arr)

    for j in range(len(maze)):
        if 2 in maze[j]:
            x = j
    
    for k in range(len(maze[x])):
        if maze[x][k] == 2:
            y = k

    for j in range(len(maze)):
        temp = []
        for k in range(len(maze[0])):
            temp.append(False) if maze[j][k] else temp.append(True)
        issued.append(temp)
    
    # print(maze)
    # print(issued)
    # print(minimum_counts)
    # print(zeros)
    # print(x, y)
    
    find_minimum_count(maze, issued, minimum_counts, zeros, x, y)
    print(f'# {i + 1} {minimum_counts[0]}')
