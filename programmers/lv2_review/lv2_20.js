// 프로그래머스 예상 대진표
function solution(n, a, b) {
  let answer = 0;
  // let start = 1;
  // let end = n;
  // let mid = a;
  // while (start <= end) {
  //   if (mid === b) {
  //     return answer;
  //   } else if (mid < b) {
  //     start = mid + 1;
  //     mid = Math.floor((start + end) / 2);
  //     answer += 1;
  //   } else if (mid > b) {
  //     end = mid - 1;
  //     mid = Math.floor((start + end) / 2);
  //     answer += 1;
  //   }
  // }
  return answer;
}

const n = 8;
const a = 1;
const b = 2;
console.log(solution(n, a, b));
