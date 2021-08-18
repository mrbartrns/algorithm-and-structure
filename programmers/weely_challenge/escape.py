# [카카오] 미로 탈출
import heapq

INF = 987654321


def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n + 1)]
    is_trap = [False] * 1010
    states = [0] * 1010
    distance = [[INF for _ in range(1 << len(traps))] for _ in range(n + 1)]

    # initialize
    for i in range(len(traps)):
        trap = traps[i]
        is_trap[trap] = True
        states[trap] = i

    for a, b, c in roads:
        graph[a].append((b, c, True))  # True road
        graph[b].append((a, c, False))  # False road

    dijkstra(start, distance, graph, is_trap, states)
    return get_min_value(distance, end)


def dijkstra(start, distance, graph, is_trap, states):
    q = []
    distance[start][0] = 0  # all trap is inactive
    heapq.heappush(q, (0, start, 0))  # cost, node, state

    while q:
        dist, now, state = heapq.heappop(q)

        for i in range(len(graph[now])):
            nxt = graph[now][i][0]
            cost = dist + graph[now][i][1]
            nxt_state = state
            edge_state = graph[now][i][2]

            case = find_case(now, nxt, is_trap)

            if case == 1:  # cur: x, nxt: x
                if edge_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            elif case == 2:  # cur: x, nxt: trap
                trap_state = is_active(nxt_state, nxt, states)
                if trap_state != edge_state:
                    if trap_state:
                        nxt_state = deactivate(nxt_state, nxt, states)
                    else:
                        nxt_state = activate(nxt_state, nxt, states)

                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            elif case == 3:  # cur: trap, nxt: x
                trap_state = is_active(nxt_state, now, states)
                if trap_state != edge_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            else:
                cur_trap_state = is_active(nxt_state, now, states)
                nxt_trap_state = is_active(nxt_state, nxt, states)
                if (cur_trap_state == nxt_trap_state) and edge_state:
                    if nxt_trap_state:
                        nxt_state = deactivate(nxt_state, nxt, states)
                    else:
                        nxt_state = activate(nxt_state, nxt, states)

                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
                elif (cur_trap_state != nxt_trap_state) and not edge_state:
                    if nxt_trap_state:
                        nxt_state = deactivate(nxt_state, nxt, states)
                    else:
                        nxt_state = activate(nxt_state, nxt, states)

                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))


def get_min_value(distance, e):
    answer = INF
    for i in range(len(distance[e])):
        answer = min(answer, distance[e][i])
    return answer


def find_case(cur, nxt, is_trap):
    if not is_trap[cur] and (not is_trap[nxt]):
        return 1
    if not is_trap[cur] and is_trap[nxt]:
        return 2
    if is_trap[cur] and (not is_trap[nxt]):
        return 3
    if is_trap[cur] and is_trap[nxt]:
        return 4


def is_active(state, idx, states):
    if state & (1 << states[idx]):
        return True
    return False


def activate(state, idx, states):
    return state | (1 << states[idx])


def deactivate(state, idx, states):
    return state ^ (1 << states[idx])


if __name__ == '__main__':
    n = 4
    start = 1
    end = 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2, 3]
    print((solution(n, start, end, roads, traps)))
