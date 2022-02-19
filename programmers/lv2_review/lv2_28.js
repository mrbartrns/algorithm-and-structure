function solution(brown, yellow) {
  const answer = [];
  for (let ver = 1; ver < Math.sqrt(yellow) + 1; ver++) {
    if (yellow % ver > 0) continue;
    let hor = Math.floor(yellow / ver);
    if ((hor + 2) * (ver + 2) === brown + yellow) {
      answer.push(hor + 2);
      answer.push(ver + 2);
      break;
    }
  }
  return answer;
}

const brown = 24;
const yellow = 24;
console.log(solution(brown, yellow));
