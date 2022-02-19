function solution(number, k) {
  let count = k;
  const stack = [];
  for (let i = 0; i < number.length; i++) {
    while (count > 0 && stack.length && stack[stack.length - 1] < number[i]) {
      stack.pop();
      count -= 1;
    }
    stack.push(number[i]);
  }
  for (let _ = 0; _ < count; _++) {
    stack.pop();
  }
  return stack.join("");
}

const number = "1924";
const k = 2;
console.log(solution(number, k));
