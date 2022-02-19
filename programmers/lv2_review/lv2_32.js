function solution(numbers) {
  var answer = [];
  numbers.forEach((number) => {
    let str = "0" + number.toString(2);
    const l = str.length;
    if (str[l - 1] === "0") {
      answer.push(number + 1);
    } else {
      for (let i = str.length; i >= 0; i--) {
        if (str[i] === "0") {
          answer.push(
            parseInt(
              str.substring(0, i) + "1" + "0" + str.substring(i + 2, l),
              2
            )
          );
          break;
        }
      }
    }
  });
  return answer;
}

const numbers = [
  1001, 337, 0, 1, 333, 673, 343, 221, 898, 997, 121, 1015, 665, 779, 891, 421,
  222, 256, 512, 128, 100,
];
const answer = solution(numbers);
const compare = [
  1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422,
  223, 257, 513, 129, 101,
];
let check = true;
for (let i = 0; i < answer.length; i++) {
  if (answer[i] !== compare[i]) {
    check = false;
    break;
  }
}
console.log(answer);
console.log(check);
