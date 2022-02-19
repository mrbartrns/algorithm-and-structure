// programmers 위장

const obj = {};

function solution(clothes) {
  for (let [cloth, category] of clothes) {
    if (!obj.hasOwnProperty(category)) {
      obj[category] = [];
    }
    obj[category].push(cloth);
  }
  let result = 1;
  for (let key of Object.keys(obj)) {
    result *= obj[key].length + 1;
  }
  result -= 1;
  return result;
}

const clothes = [
  ["crowmask", "face"],
  ["bluesunglasses", "face"],
  ["smoky_makeup", "face"],
];

console.log(solution(clothes));
