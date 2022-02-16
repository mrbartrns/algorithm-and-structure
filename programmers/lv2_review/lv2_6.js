function solution(numbers, target) {
  let answer = 0;
  const dfs = (idx, number) => {
    if (idx === numbers.length) {
      if (number === target) {
        answer += 1;
      }
      return;
    }
    dfs(idx + 1, number + numbers[idx]);
    dfs(idx + 1, number - numbers[idx]);
  };
  dfs(0, 0);
  return answer;
}
const numbers = [4, 1, 2, 1];
const target = 4;
console.log(solution(numbers, target));
