"""
그래프에서 DFS로 사이클 찾기
유향 그래프에서 사이클을 찾는 법
# 무향그래프에서는 별도의 정의가 있지 않는 한 서로를 왕복할 수만 있으면 사이클이 존재한다.

DFS 스패닝 트리와 간선 분류
어떤 그래프를 DFS로 탐색했을 때 edge만 남겨놓으면 트리 형태가 되는데 이를 dfs 스패닝트리라고 한다.
어떤 그래프를 DFS 스패닝 트리로 변환했을 때 그래프의 모든 엣지를 4가지로 분류할 수 있다.

## Tree edge
트리 간선은 DFS 스패닝 트리에 속하는 간선 -> (dfs를 하면서 거쳐간 간선)
## Forward edge (순방향 간선)
DFS를 통해 어떤 연결된 두 노드 사이의 부모 자식 관계를 정립할 수 있지만 스패닝 트리에서 트리는 아닌 간선
## Back edge
DFS 스패닝 트리에서 자식 -> 부모로 거슬러 올라가는 간선
## Cross edge (교차 간선)
위 세 종류를 제외한 나머지 간선들이며 형제 노드끼리 연결된 간선


# 방향 그래프에서 사이클 찾기
위 분류를 통해 방향 그래프에서 사이클이 존재하는 경우를 간단하게 정의할 수 있다.
바로 역방향 간선의 존재 여부이다. 역방향 간선의 개수는 곧 사이클의 갯수가 된다.
다음 두 정보를 관리하는 배열이 필요하다.
visited[]: 해당 노드를 방문했는지 방문하지 않았는지 여부 확인 배열
finished[]: 해당 노드를 대상으로 호출한 함수가 종료되었는지 여부를 관리하는 배열

DFS 탐색을 하면서 방문하지 않은 노드는 방문하고 만약 해당 노드가 방문된 상태인데 종료가 되지 않았다면
discovere == true && finished == false -> 역방향 간선을 찾았다는 의미
"""

# EXAMPLE


def dfs(node):
    pass
