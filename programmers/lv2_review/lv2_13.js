function solution(expression) {
  let answer = 0;
  const opArrs = permutations(["*", "-", "+"], 3);
  for (let i = 0; i < opArrs.length; i++) {
    const ops = opArrs[i];
    answer = Math.max(answer, Math.abs(solve(expression, ops)));
  }
  return answer;
}

function permutations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);
  // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    // 해당하는 fixed를 제외한 나머지 배열
    const permutationArr = permutations(rest, selectNumber - 1);
    // 나머지에 대해서 순열을 구한다.
    const attached = permutationArr.map((el) => [fixed, ...el]);
    //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
    results.push(...attached);
    // 배열 spread syntax 로 모두다 push
  });

  return results; // 결과 담긴 results return
}

function calculate(n1, n2, op) {
  switch (op) {
    case "*":
      return n1 * n2;
    case "+":
      return n1 + n2;
    case "-":
      return n1 - n2;
    default:
      throw Error("op is invalid");
  }
}

function solve(expression, opArr) {
  let flag = true;
  let ret = 0;
  for (let i = 0; i < 3; i++) {
    const expressionArr = expression.split(opArr[i]);
    if (expressionArr.length > 1) {
      ret = calculate(
        solve(expressionArr[0], opArr),
        solve(expressionArr[1], opArr),
        opArr[i]
      );
      for (let j = 2; j < expressionArr.length; j++) {
        ret = calculate(ret, solve(expressionArr[j], opArr), opArr[i]);
      }
      flag = false;
      break;
    }
  }
  if (flag) {
    return parseInt(expression);
  }
  return ret;
}

const expression = "100-200*300-500+20";
console.log(solution(expression));
