function solution(k, dungeons) {
  let answer = 0;
  for (let i = 1; i < dungeons.length + 1; i++) {
    backtrack(0, i, [], dungeons.length, 0);
  }
  for (let o of order) {
    let count = 0;
    let current = k;
    for (let j of o) {
      const [minimum, cost] = dungeons[j];
      if (current >= minimum) {
        count += 1;
        current -= cost;
      } else {
        break;
      }
    }
    answer = Math.max(answer, count);
  }
  return answer;
}

function backtrack(idx, count, arr, dungeonsLength, visited) {
  if (idx === count) {
    order.push([...arr]);
    return;
  }
  for (let i = 0; i < dungeonsLength; i++) {
    if (visited & (1 << i)) continue;
    backtrack(idx + 1, count, [...arr, i], dungeonsLength, visited | (1 << i));
  }
}

const order = [];

const k = 80;
const dungeons = [
  [80, 20],
  [50, 40],
  [30, 10],
];

console.log(solution(k, dungeons));
