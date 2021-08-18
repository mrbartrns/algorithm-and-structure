# [카카오] 미로 탈출
"""
미로의 노드를 탐색하는데 있어 총 4가지 경우가 존재
1) cur 가 함정이 아니고, next 가 함정이 아니다.
- 이 경우에는 현재 간선이 올바른 간선일 경우에만 탐색이 가능
- cur, next 모두 함정이 아니기 때문에 두 개를 연결하고 있는 간선의 방향이 바뀔 가능성은 없다.
2) cur 가 함정이 아니고, next 만 함정
- 올바르지 않은 간선 형태로 바뀌어져 있는 상태를 활성화 되어있는 상태로 표현할 때,
- 아직 함정 node를 한번도 방문하지 않았거나,
- 함정 칸을 짝수번 방문함으로써 node간 연결되어 있는 모든 간선들의 방향이 정방향일 때는
- 비활성화된 상태로 표현할 수 있다.
- next node는 함정 노드이기때문에 이 노드를 몇번 방문했는지에 따라서 해당 함정 node가 활성화 되어있는지에 따라 결과가 달라짐
2-1) next가 함정이면서 이 node가 활성화 되어 있는 함정 노드인 경우
- 활성되어 있다는 뜻은 기존에 한번 방문했기 때문에 이 노드와 연결되어 있는 간선들은 올바르지 않은 간선일 것이다.
- cur > next로 가기위해서는 이 간선이 올바르지 않은 간선 형태여야만 한다.
2-2) next가 함정이면서 이 node가 활성화 되어 있지 않은 경우
- 올바른 간선을 통해서만 탐색이 가능
3) cur이 함정이고, next는 함정이 아닌 경우
- 마찬가지로 활성화 되어 있다면 올바르지 않은 간선, 활성화 되어 있지 않으면 올바른 간선을 통하여 이동 가능
4) cur가 함정이고, next가 함정인 경우
- 총 4가지 경우가 가능
- i. cur, next 모두 활성화
- ii. cur만 활성화, next는 비활성화
- iii. cur이 비활성화, next는 활성화
- iv: cur이 비활성화, next도 비활성화 상태
4-1) cur, next 모두 활성화 되어있는 상태일 경우
- 올바른 간선(두번 바뀌었으므로) 연결되어 있는 형태일 것이다.
- 올바른 간선일 경우에만 탐색이 가능
4-2) cur만 활성화 되어 있고, next는 비활성화 되어있는 함정 node인 경우
- 올바르지 않은 간선일 경우만 탐색이 가능
4-3) cur은 활성화 되어있지 않고, next는 활성화 되어있는 경우
- 올바르지 않은 경우만 가능
4-4) cur, next 모두 비활성화
- 올바른 간선 형태로 존재할 것이기 때문에 현재 탐색하려는 간선이 올바른 간선일 경우에만 탐색이 가능

결론:
cur과 next 상태가 동일한 경우 > 올바른 간선을 통해 이동이 가능
cur과 next 상태가 동일하지 않은 경우 > 올바르지 않은 간선을 통해 이동이 가능
1. 탐색에 어느 하나라도 함정 node가 포함되는 순간, 이 노드가 활성화/비활성화인지 체크 필요
"""
import heapq

INF = 987654321
MAX = 1010
TRAP_MAX = 10


def solution(n, start, end, roads, traps):
    # setting
    graph = [[] for _ in range(MAX)]
    for a, b, c in roads:
        graph[a].append((b, c, True))
        graph[b].append((a, c, False))
    is_trap = [False] * MAX
    trap_idx = [0] * MAX
    distance = [[INF for _ in range(1 << TRAP_MAX)] for _ in range(MAX)]
    for i in range(len(traps)):
        trap = traps[i]
        is_trap[trap] = True
        trap_idx[trap] = i
    return dijkstra(start, end, distance, graph, trap_idx)


def trap_state(nxt, state, trap_idx):
    if not (state & (1 << trap_idx[nxt])):
        return False
    return True


def active_trap(state, idx, trap_idx):
    return state | (1 << trap_idx[idx])


def inactive_trap(state, idx, trap_idx):
    return state ^ (1 << trap_idx[idx])


def find_case(cur, nxt, is_trap):
    if not is_trap[cur] and not is_trap[nxt]:
        return 1
    if not is_trap[cur] and is_trap[nxt]:
        return 2
    if is_trap[cur] and not is_trap[nxt]:
        return 3
    if is_trap[cur] and is_trap[nxt]:
        return 4


def find_min_cost(e, distance):
    ret = INF
    for i in range(len(distance[e])):
        ret = min(ret, distance[e][i])
    return ret


def dijkstra(s, e, distance, graph, trap_idx):
    q = []
    heapq.heappush(q, (0, s, 0))  # cost, now, state
    distance[s][0] = 0
    while q:
        dist, now, state = heapq.heappop(q)
        for i in range(len(graph[now])):
            nxt = graph[now][i][0]
            cost = graph[now][i][1] + now
            nxt_state = state
            edge_state = graph[now][i][2]

            case = find_case(now, nxt, state)
            if case == 1:
                if edge_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (nxt, cost, nxt_state))
            elif case == 2:
                nxt_trap_state = trap_state(nxt, state, trap_idx)
                if edge_state != nxt_trap_state:
                    if nxt_trap_state:
                        nxt_state = inactive_trap(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = active_trap(nxt_state, nxt, trap_idx)

                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))

            elif case == 3:
                cur_trap_state = trap_state(now, state, trap_idx)
                if edge_state != cur_trap_state:
                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
            else:
                cur_trap_state = trap_state(now, state, trap_idx)
                nxt_trap_state = trap_state(nxt, state, trap_idx)

                if (cur_trap_state == nxt_trap_state) and edge_state:
                    if nxt_trap_state:
                        nxt_state = inactive_trap(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = active_trap(nxt_state, nxt, trap_idx)

                    if distance[nxt][nxt_state] > cost:
                        distance[nxt][nxt_state] = cost
                        heapq.heappush(q, (cost, nxt, nxt_state))
    return find_min_cost(e, distance)


if __name__ == '__main__':
    n = 3
    start = 1
    end = 3
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2]
    print(solution(n, start, end, roads, traps))
