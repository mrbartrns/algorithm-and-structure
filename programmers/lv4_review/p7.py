# [카카오] 미로 탈출
import heapq

INF = 987654321


def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n + 1)]
    is_trap = [False] * (n + 1)
    trap_idx = [0] * (n + 1)
    for a, b, c in roads:
        graph[a].append((b, c, True))
        graph[b].append((a, c, False))
    for i in range(len(traps)):
        trap = traps[i]
        is_trap[trap] = True
        trap_idx[trap] = i
    distance = [[INF for _ in range(1 << len(traps))] for _ in range(n + 1)]
    dijkstra(start, distance, graph, trap_idx=trap_idx, is_trap=is_trap)
    answer = INF
    for i in range(len(distance[0])):
        answer = min(answer, distance[end][i])
    return answer


# 본인의 상태도 중요함!
def dijkstra(start, distance, graph, **kwargs):
    q = []
    distance[start][0] = 0
    heapq.heappush(q, (0, start, 0))
    while q:
        dist, now, state = heapq.heappop(q)

        for i in range(len(graph[now])):
            nxt = graph[now][i][0]
            cost = dist + graph[now][i][1]
            nxt_state = state
            edge_state = graph[now][i][2]

            case = check_trap(now, nxt, kwargs['is_trap'])

            if case == 1:
                if edge_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            elif case == 2:
                nxt_trap_state = is_active(nxt_state, nxt, kwargs['trap_idx'])
                if nxt_trap_state != edge_state:
                    if edge_state:
                        nxt_state = activate(nxt_state, nxt, kwargs['trap_idx'])
                    else:
                        nxt_state = deactivate(nxt_state, nxt, kwargs['trap_idx'])
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            elif case == 3:
                cur_trap_state = is_active(nxt_state, now, kwargs['trap_idx'])
                if cur_trap_state != edge_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            else:
                cur_trap_state = is_active(nxt_state, now, kwargs['trap_idx'])
                nxt_trap_state = is_active(nxt_state, nxt, kwargs['trap_idx'])
                if (cur_trap_state == nxt_trap_state) and edge_state:
                    if not nxt_trap_state:
                        nxt_state = activate(nxt_state, nxt, kwargs['trap_idx'])
                    else:
                        nxt_state = deactivate(nxt_state, nxt, kwargs['trap_idx'])
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
                elif (cur_trap_state != nxt_trap_state) and not edge_state:
                    if not nxt_trap_state:
                        nxt_state = activate(nxt_state, nxt, kwargs['trap_idx'])
                    else:
                        nxt_state = deactivate(nxt_state, nxt, kwargs['trap_idx'])
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))


def activate(state, node, trap_idx):
    return state | (1 << trap_idx[node])


def deactivate(state, node, trap_idx):
    return state ^ (1 << trap_idx[node])


def is_active(state, node, trap_idx):
    if state & (1 << trap_idx[node]):
        return True
    return False


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
    n = 3
    start = 1
    end = 3
    roads = [[1, 2, 2], [3, 2, 3]]
    traps = [2]
    print(solution(n, start, end, roads, traps))
