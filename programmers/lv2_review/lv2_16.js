// programmers printer
function solution(priorities, location) {
  let answer = 0;
  const q = priorities.map((el, index) => [el, index]);
  const p = Array(10).fill(0);
  for (let i = 0; i < priorities.length; i++) {
    p[priorities[i]] += 1;
  }
  while (q.length) {
    const [priority, index] = q.shift();
    let flag = true;
    for (let i = priority + 1; i < 10; i++) {
      if (p[i]) {
        q.push([priority, index]);
        flag = false;
        break;
      }
    }
    if (flag) {
      answer += 1;
      p[priority] -= 1;
      if (index === location) {
        return answer;
      }
    }
  }
  return answer;
}

const priorities = [1, 1, 9, 1, 1, 1];
const location = 0;
console.log(solution(priorities, location));
