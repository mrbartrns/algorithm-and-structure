function solution(p) {
  let answer = "";
  if (p === "") return "";
  let u = "";
  let v = "";
  const stack = [];
  let left = 0;
  let right = 0;
  let index = 0;
  while (index < p.length) {
    if (p[index] === "(") left += 1;
    else if (p[index] === ")") right += 1;
    u += p[index];
    index++;
    if (left === right) break;
  }
  while (index < p.length) {
    v += p[index];
    index++;
  }
  for (let i = 0; i < left + right; i++) {
    if (stack.length && stack[stack.length - 1] === "(" && p[i] === ")") {
      stack.pop();
    } else {
      stack.push(p[i]);
    }
  }
  if (!stack.length) {
    answer = u + solution(v);
    return answer;
  }
  answer += "(";
  answer += solution(v);
  answer += ")";
  for (let i = 1; i < u.length - 1; i++) {
    answer += p[i] === "(" ? ")" : "(";
  }

  return answer;
}

const p = "()))((()";
console.log(solution(p));
