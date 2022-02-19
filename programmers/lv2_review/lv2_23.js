// 괄호 회전하기
function solution(s) {
  let answer = 0;
  const q = s.split("");
  for (let i = 0; i < s.length; i++) {
    const e = q.shift();
    q.push(e);
    if (isCorrectBraket(q)) {
      answer += 1;
    }
  }
  return answer;
}

function isCorrectBraket(q) {
  const stack = [];
  for (let i = 0; i < q.length; i++) {
    if (stack.length) {
      if (stack[stack.length - 1] === "[" && q[i] === "]") {
        stack.pop();
      } else if (stack[stack.length - 1] === "{" && q[i] === "}") {
        stack.pop();
      } else if (stack[stack.length - 1] === "(" && q[i] === ")") {
        stack.pop();
      } else {
        stack.push(q[i]);
      }
    } else {
      stack.push(q[i]);
    }
  }
  return stack.length ? false : true;
}
const s = "[](){}";
console.log(solution(s));
