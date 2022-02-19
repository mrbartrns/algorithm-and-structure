function solution(m, n, board) {
  let answer = 0;
  const checkBoard = Array.from({ length: m }, () => Array(n).fill(false));
  const copyBoard = board.map((el) => el.split(""));
  while (true) {
    let check = false;
    // check on check board
    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        if (copyBoard[i][j] === "") continue;
        if (
          copyBoard[i][j] === copyBoard[i + 1][j] &&
          copyBoard[i + 1][j] === copyBoard[i][j + 1] &&
          copyBoard[i][j + 1] === copyBoard[i + 1][j + 1]
        ) {
          checkBoard[i][j] = true;
          checkBoard[i + 1][j] = true;
          checkBoard[i][j + 1] = true;
          checkBoard[i + 1][j + 1] = true;
          check = true;
        }
      }
    }
    if (!check) break;
    answer += erase(copyBoard, checkBoard);
    scrollDown(copyBoard);
    memeset(checkBoard, false);
  }
  return answer;
}

function erase(board, checkBoard) {
  let count = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (checkBoard[i][j]) {
        board[i][j] = "";
        count += 1;
      }
    }
  }
  return count;
}

function memeset(arr, value) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      arr[i][j] = value;
    }
  }
}

function scrollDown(board) {
  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board[0].length; x++) {
      if (board[y][x] === "") {
        for (let k = y; k > 0; k--) {
          board[k][x] = board[k - 1][x];
        }
        board[0][x] = "";
      }
    }
  }
}

const m = 4; // row
const n = 5; // col
const board = ["CCBDE", "AAADE", "AAABF", "CCBBF"];

console.log(solution(m, n, board));
