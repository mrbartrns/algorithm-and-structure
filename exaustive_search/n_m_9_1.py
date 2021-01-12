n, m = map(int, input().split())
my_list = list(map(int, input().split()))
double_check = []
my_list.sort()
solve = []
visited = [0] * n


def Dfs(depth):
    if depth == m:
        print(" ".join(map(str, solve)))
        return
    append_count = 0
    double_check.append(-1)
    print(double_check)
    for i in range(n):
        if visited[i] == 0:
            if double_check[len(double_check) - 1] != my_list[i]:
                double_check.append((my_list[i]))
                append_count += 1
                print(double_check)
                solve.append(my_list[i])
                visited[i] = my_list[i]
                Dfs(depth + 1)
                visited[i] = 0
                solve.pop()
    for _ in range(append_count + 1):
        double_check.pop()


Dfs(0)