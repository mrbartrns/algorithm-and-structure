# [카카오] 미로 탈출
import heapq

INF = 987654321


def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n + 1)]
    is_trap = [False] * (n + 1)
    trap_idx = [0] * (n + 1)
    distance = [[INF for _ in range(1 << len(traps))] for _ in range(n + 1)]

    for i in range(len(traps)):
        trap = traps[i]
        is_trap[trap] = True
        trap_idx[trap] = i

    for a, b, c in roads:
        graph[a].append((b, c, True))
        graph[b].append((a, c, False))

    dijkstra(start, distance, graph, is_trap, trap_idx)
    return get_min_value(distance, end)


def dijkstra(start, distance, graph, is_trap, trap_idx):
    q = []
    distance[start][0] = 0
    heapq.heappush(q, (0, start, 0))
    while q:
        dist, cur, state = heapq.heappop(q)
        for i in range(len(graph[cur])):
            nxt = graph[cur][i][0]
            cost = dist + graph[cur][i][1]
            nxt_state = state
            edge_state = graph[cur][i][2]

            case = check_trap(cur, nxt, is_trap)
            if case == 1:
                if edge_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            elif case == 2:
                trap_state = is_active(nxt_state, nxt, trap_idx)
                if trap_state != edge_state:
                    if edge_state:
                        nxt_state = activate_switch(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = deactivate_switch(nxt_state, nxt, trap_idx)

                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            elif case == 3:
                trap_state = is_active(nxt_state, cur, trap_idx)
                if trap_state != edge_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            else:
                cur_trap_state = is_active(nxt_state, cur, trap_idx)
                nxt_trap_state = is_active(nxt_state, nxt, trap_idx)
                if (cur_trap_state == nxt_trap_state) and edge_state:
                    if nxt_trap_state:
                        nxt_state = deactivate_switch(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = activate_switch(nxt_state, nxt, trap_idx)
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))

                elif (cur_trap_state != nxt_trap_state) and not edge_state:
                    if nxt_trap_state:
                        nxt_state = deactivate_switch(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = activate_switch(nxt_state, nxt, trap_idx)
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))


def get_min_value(distance, e):
    ret = INF
    for i in range(len(distance[e])):
        ret = min(ret, distance[e][i])
    return ret


def is_active(state, node, trap_idx):
    if state & (1 << trap_idx[node]):
        return True
    return False


def activate_switch(state, node, trap_idx):
    return state | (1 << trap_idx[node])


def deactivate_switch(state, node, trap_idx):
    return state ^ (1 << trap_idx[node])


def check_trap(cur, nxt, is_trap):
    if not is_trap[cur] and not is_trap[nxt]:
        return 1
    if not is_trap[cur] and is_trap[nxt]:
        return 2
    if is_trap[cur] and not is_trap[nxt]:
        return 3
    if is_trap[cur] and is_trap[nxt]:
        return 4


if __name__ == '__main__':
    n = 4
    start = 1
    end = 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2, 3]
    print(solution(n, start, end, roads, traps))
