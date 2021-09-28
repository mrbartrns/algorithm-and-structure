# [카카오] 미로 탈출
# 클래스 호출 시간 때문에 클래스를 사용하면 손해
import heapq


class Maze:
    INF = 987654321

    def __init__(self, n, trap_counts) -> None:
        self.graph = [[] for _ in range(n + 1)]
        self.distance = [
            [Maze.INF for _ in range(1 << trap_counts)] for _ in range(n + 1)
        ]
        self.is_trap = [False] * (n + 1)
        self.trap_idx = [0] * (n + 1)

    def set_trap(self, traps):
        for i in range(len(traps)):
            trap = traps[i]
            self.is_trap[trap] = True
            self.trap_idx[trap] = i

    def set_graph(self, roads):
        for a, b, c in roads:
            self.graph[a].append((b, c, True))
            self.graph[b].append((a, c, False))

    def check_case(self, cur, nxt):
        if not self.is_trap[cur] and not self.is_trap[nxt]:
            return 1
        if not self.is_trap[cur] and self.is_trap[nxt]:
            return 2
        if self.is_trap[cur] and not self.is_trap[nxt]:
            return 3
        if self.is_trap[cur] and self.is_trap[nxt]:
            return 4

    def check_trap_state(self, trap, state):
        if state & (1 << self.trap_idx[trap]):
            return True
        return False

    def activate(self, trap, state):
        return state | (1 << self.trap_idx[trap])

    def deactivate(self, trap, state):
        return state ^ (1 << self.trap_idx[trap])

    def dijkstra(self, start):
        q = []
        self.distance[start][0] = 0
        heapq.heappush(q, (0, start, 0))  # cost, node, state
        while q:
            dist, cur, state = heapq.heappop(q)

            for i in range(len(self.graph[cur])):
                nxt = self.graph[cur][i][0]
                cost = self.graph[cur][i][1] + dist
                nxt_state = state
                edge_state = self.graph[cur][i][2]

                case = self.check_case(cur, nxt)

                if case == 1:
                    if edge_state:
                        if self.distance[nxt][nxt_state] > cost:
                            self.distance[nxt][nxt_state] = cost
                            heapq.heappush(q, (cost, nxt, nxt_state))
                elif case == 2:
                    nxt_trap_state = self.check_trap_state(nxt, nxt_state)
                    if nxt_trap_state != edge_state:
                        if edge_state:  # edge_state가 True라면 nxt_trap_state = False
                            nxt_state = self.activate(nxt, nxt_state)
                        else:
                            nxt_state = self.deactivate(nxt, nxt_state)
                        if self.distance[nxt][nxt_state] > cost:
                            self.distance[nxt][nxt_state] = cost
                            heapq.heappush(q, (cost, nxt, nxt_state))
                elif case == 3:
                    cur_trap_state = self.check_trap_state(cur, nxt_state)
                    if cur_trap_state != edge_state:
                        if self.distance[nxt][nxt_state] > cost:
                            self.distance[nxt][nxt_state] = cost
                            heapq.heappush(q, (cost, nxt, nxt_state))
                else:
                    cur_trap_state = self.check_trap_state(cur, nxt_state)
                    nxt_trap_state = self.check_trap_state(nxt, nxt_state)
                    if (cur_trap_state == nxt_trap_state) and edge_state:
                        if nxt_trap_state:
                            nxt_state = self.deactivate(nxt, nxt_state)
                        else:
                            nxt_state = self.activate(nxt, nxt_state)
                        if self.distance[nxt][nxt_state] > cost:
                            self.distance[nxt][nxt_state] = cost
                            heapq.heappush(q, (cost, nxt, nxt_state))
                    elif (cur_trap_state != nxt_trap_state) and not edge_state:
                        if nxt_trap_state:
                            nxt_state = self.deactivate(nxt, nxt_state)
                        else:
                            nxt_state = self.activate(nxt, nxt_state)
                        if self.distance[nxt][nxt_state] > cost:
                            self.distance[nxt][nxt_state] = cost
                            heapq.heappush(q, (cost, nxt, nxt_state))

    def get_value(self, end):
        answer = Maze.INF
        for i in range(len(self.distance[end])):
            answer = min(answer, self.distance[end][i])
        return answer


def solution(n, start, end, roads, traps):
    maze = Maze(n, len(traps))
    maze.set_graph(roads)
    maze.set_trap(traps)
    maze.dijkstra(start)
    return maze.get_value(end)


if __name__ == "__main__":
    n = 4
    start = 1
    end = 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2, 3]
    print(solution(n, start, end, roads, traps))