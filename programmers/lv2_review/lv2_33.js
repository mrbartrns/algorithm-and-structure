function solution(n) {
  const answer = [];
  const board = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
  let top = 1;
  let bottom = n;
  let left = 1;
  let right = 0;
  let count = 1;
  let state = 0;
  while (count <= Math.floor((n * (n + 1)) / 2)) {
    if (state === 0) {
      for (let i = top; i < bottom + 1; i++) {
        board[i][left] = count;
        count += 1;
      }
      left += 1;
      top += 1;
      state = (1 + state) % 3;
    } else if (state === 1) {
      for (let i = left; i < bottom - right + 1; i++) {
        board[bottom][i] = count;
        count += 1;
      }
      bottom -= 1;
      state = (1 + state) % 3;
    } else if (state === 2) {
      for (let i = bottom; i > top - 1; i--) {
        board[i][i - right] = count;
        count += 1;
      }
      right += 1;
      top += 1;
      state = (state + 1) % 3;
    }
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[i][j] > 0) {
        answer.push(board[i][j]);
      }
    }
  }

  return answer;
}

const n = 6;
console.log(solution(n));
