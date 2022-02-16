function solution(progresses, speeds) {
  const answer = [];
  while (progresses.length) {
    const left = 100 - progresses[0];
    const days =
      Math.floor(left / speeds[0]) + (left % speeds[0] === 0 ? 0 : 1);
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i] * days;
    }
    let count = 0;
    while (progresses.length) {
      if (progresses[0] < 100) {
        break;
      }
      count += 1;
      progresses.shift();
      speeds.shift();
    }
    answer.push(count);
  }
  return answer;
}

const progresses = [100];
const speeds = [1];
console.log(solution(progresses, speeds));
