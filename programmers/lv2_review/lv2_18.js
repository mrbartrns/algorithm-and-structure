function solution(numbers) {
  let answer = 0;
  const set = new Set();
  for (let i = 1; i < numbers.length + 1; i++) {
    const visited = Array(numbers.length).fill(false);
    backtrack(0, i, visited, "", set, numbers);
  }
  for (let c of set) {
    if (c <= 1) continue;
    if (c === 2) {
      answer += 1;
      continue;
    }
    let flag = true;
    for (let j = 2; j < Math.floor(Math.sqrt(c)) + 1; j++) {
      if (c % j === 0) {
        flag = false;
        break;
      }
    }
    if (flag) {
      answer += 1;
    }
  }
  return answer;
}

function backtrack(idx, count, visited, subString, set, string) {
  if (idx === count) {
    set.add(parseInt(subString));
    return;
  }
  for (let i = 0; i < visited.length; i++) {
    if (!visited[i]) {
      visited[i] = true;
      backtrack(idx + 1, count, visited, subString + string[i], set, string);
      visited[i] = false;
    }
  }
}

const numbers = "011";
console.log(solution(numbers));
