const INF = 987654321;
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

function solution(maps) {
  const q = [];
  const visited = Array.from({ length: maps.length }, () =>
    Array(maps[0].length).fill(INF)
  );
  visited[0][0] = 1;
  q.push([0, 0, 1]);
  while (q.length) {
    const [y, x, cnt] = q.shift();
    for (let i = 0; i < 4; i++) {
      ny = y + dy[i];
      nx = x + dx[i];
      if (ny < 0 || ny >= maps.length || nx < 0 || nx >= maps[0].length)
        continue;
      if (maps[ny][nx] === 0) continue;
      if (visited[ny][nx] > cnt + 1) {
        visited[ny][nx] = cnt + 1;
        q.push([ny, nx, cnt + 1]);
      }
    }
  }
  const answer = visited[maps.length - 1][maps[0].length - 1];
  return answer < INF ? answer : -1;
}

const maps = [
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1],
];
console.log(bfs(maps));
