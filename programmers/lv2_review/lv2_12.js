// programmers 거리두기 확인하기
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];
const INF = 987654321;

function solution(places) {
  const answer = [];
  for (let i = 0; i < places.length; i++) {
    answer.push(check(places[i]) ? 1 : 0);
  }
  return answer;
}

function check(place) {
  let flag = true;
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (place[i][j] === "P") {
        if (!bfs(i, j, place)) {
          flag = false;
          break;
        }
      }
    }
    if (!flag) break;
  }
  return flag;
}

function bfs(sy, sx, place) {
  const q = [];
  const visited = [];
  for (let i = 0; i < 5; i++) {
    const temp = [];
    for (let j = 0; j < 5; j++) {
      temp.push(false);
    }
    visited.push(temp);
  }
  q.push([sy, sx, 0]);
  visited[sy][sx] = true;
  while (q.length) {
    const [y, x, cnt] = q.shift();
    if (sy !== y && sx !== x && place[y][x] === "P") return false;
    if (cnt >= 2) continue;
    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];
      if (ny < 0 || ny >= 5 || nx < 0 || nx >= 5) continue;
      if (place[ny][nx] === "X") continue;
      if (!visited[ny][nx]) {
        visited[ny][nx] = true;
        q.push([ny, nx, cnt + 1]);
      }
    }
  }
  return true;
}

const places = [
  ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
];

console.log(solution(places));

/**
 * ["XOOXX", "XPOOP", "OXXPX", "XXXXX", "XXXXX"]
 */
