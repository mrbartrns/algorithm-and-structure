class Heap {
  constructor() {
    this.heap = [null];
  }

  size() {
    return this.heap.length - 1;
  }

  getMin() {
    return this.heap[1] ? this.heap[1] : null;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  heappush(value) {
    this.heap.push(value);
    let curIdx = this.heap.length - 1;
    let parIdx = (curIdx / 2) >> 0;

    while (curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
      this.swap(parIdx, curIdx);
      curIdx = parIdx;
      parIdx = (curIdx / 2) >> 0;
    }
  }

  heappop() {
    const min = this.heap[1];
    if (this.heap.length <= 2) this.heap = [null];
    else this.heap[1] = this.heap.pop();

    let curIdx = 1;
    let leftIdx = curIdx * 2;
    let rightIdx = curIdx * 2 + 1;

    if (!this.heap[leftIdx]) return min;
    if (!this.heap[rightIdx]) {
      if (this.heap[leftIdx] < this.heap[curIdx]) {
        this.swap(leftIdx, curIdx);
      }
      return min;
    }

    while (
      this.heap[leftIdx] < this.heap[curIdx] ||
      this.heap[rightIdx] < this.heap[curIdx]
    ) {
      const minIdx =
        this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
      this.swap(minIdx, curIdx);
      curIdx = minIdx;
      leftIdx = curIdx * 2;
      rightIdx = curIdx * 2 + 1;
    }

    return min;
  }
}
const INF = 987654321;
function solution(N, road, K) {
  let answer = 0;
  const adj = Array.from({ length: N + 1 }, () => []);
  road.forEach(([a, b, c]) => {
    adj[a].push([b, c]);
    adj[b].push([a, c]);
  });
  const distance = Array.from({ length: N + 1 }, () => INF);
  dijkstra(distance, adj);
  for (let i = 1; i <= N; i++) {
    if (distance[i] <= K) {
      answer += 1;
    }
  }

  return answer;
}

function dijkstra(distance, adj) {
  const heapq = new Heap();
  distance[1] = 0;
  heapq.heappush([0, 1]);
  while (heapq.size()) {
    const [cnt, node] = heapq.heappop();
    if (cnt > distance[node]) continue;
    for (let [nxt, dist] of adj[node]) {
      const value = dist + cnt;
      if (distance[nxt] > value) {
        distance[nxt] = value;
        heapq.heappush([value, nxt]);
      }
    }
  }
}

const N = 5;
const road = [
  [1, 2, 1],
  [2, 3, 3],
  [5, 2, 2],
  [1, 4, 2],
  [5, 3, 1],
  [5, 4, 2],
];
const K = 3;
console.log(solution(N, road, K));
