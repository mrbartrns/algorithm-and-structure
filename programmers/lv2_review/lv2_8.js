function solution(rows, columns, queries) {
  let count = 0;
  const answer = [];
  const matrix = [];
  for (let i = 0; i < rows; i++) {
    const row = [];
    for (let j = 0; j < columns; j++) {
      count += 1;
      row.push(count);
    }
    matrix.push(row);
  }
  for (let i = 0; i < queries.length; i++) {
    const [y1, x1, y2, x2] = queries[i];
    answer.push(rotate(y1 - 1, x1 - 1, y2 - 1, x2 - 1, matrix));
  }
  return answer;
}

function rotate(y1, x1, y2, x2, matrix) {
  const INF = 987654321;
  let min = INF;
  const q = [];
  for (let i = x1; i < x2; i++) {
    q.push(matrix[y1][i]);
  }
  for (let i = y1; i < y2; i++) {
    q.push(matrix[i][x2]);
  }
  for (let i = x2; i > x1; i--) {
    q.push(matrix[y2][i]);
  }
  for (let i = y2; i > y1; i--) {
    q.push(matrix[i][x1]);
  }
  const last = q.pop();
  q.unshift(last);
  let index = 0;
  for (let i = x1; i < x2; i++) {
    matrix[y1][i] = q[index];
    min = Math.min(min, q[index]);
    index++;
  }
  for (let i = y1; i < y2; i++) {
    matrix[i][x2] = q[index];
    min = Math.min(min, q[index]);
    index += 1;
  }
  for (let i = x2; i > x1; i--) {
    matrix[y2][i] = q[index];
    min = Math.min(min, q[index]);
    index += 1;
  }
  for (let i = y2; i > y1; i--) {
    matrix[i][x1] = q[index];
    min = Math.min(min, q[index]);
    index += 1;
  }
  return min;
}

const rows = 100;
const columns = 97;
const queries = [[1, 1, 100, 97]];
console.log(solution(rows, columns, queries));
