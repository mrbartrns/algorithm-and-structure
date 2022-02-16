function solution(n) {
  if (n === 0) return "";
  let string = "";
  if (n % 3 === 1) {
    string = "1";
  } else if (n % 3 === 2) {
    string = "2";
  } else if (n % 3 === 0) {
    string = "4";
  }
  if (n % 3 === 0) {
    string = solution(Math.floor(n / 3) - 1) + string;
  } else {
    string = solution(Math.floor(n / 3)) + string;
  }
  return string;
}

console.log(solution(4));
