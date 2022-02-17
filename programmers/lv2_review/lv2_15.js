function solution(grid) {
  const answer = [];
  const visited = Array.from({ length: grid.length }, () =>
    Array.from({ length: grid[0].length }, () => Array(4).fill(0))
  );
  console.log(visited);
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      for (let k = 0; k < 4; k++) {
        if (!visited[i][j][k]) {
          bfs(i, j, k, visited, grid);
          answer.push(visited[i][j][k]);
        }
      }
    }
  }
  answer.sort((a, b) => a - b);
  return answer;
}

function bfs(sy, sx, sd, visited, grid) {
  const q = [];
  const [row, col] = [grid.length, grid[0].length];
  const dy = [row - 1, 0, 1, 0];
  const dx = [0, col - 1, 0, 1];
  q.push([sy, sx, sd, 0]); // y, x, direction, count
  while (q.length) {
    const [y, x, d, cnt] = q.shift();
    let ny, nx, nd;
    if (grid[y][x] === "S") {
      nd = d;
      ny = (y + dy[nd]) % row;
      nx = (x + dx[nd]) % col;
    } else if (grid[y][x] === "L") {
      nd = (d + 1) % 4;
      ny = (y + dy[nd]) % row;
      nx = (x + dx[nd]) % col;
    } else {
      nd = (d + 3) % 4;
      ny = (y + dy[nd]) % row;
      nx = (x + dx[nd]) % col;
    }
    if (!visited[ny][nx][nd]) {
      visited[ny][nx][nd] = cnt + 1;
      q.push([ny, nx, nd, cnt + 1]);
    }
  }
}

const grid = ["R", "R"];
console.log(solution(grid));
