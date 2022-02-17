// 정렬되어있는 것의 개수를 센다 => bisect_left, bisect_right

function solution(s) {
  const temp = s.substring(2, s.length - 2);
  const tempArr = temp.split("},{");
  const arr = tempArr.map((el) => {
    return el.split(",");
  });
  const obj = {};
  const set = new Set();
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      set.add(parseInt(arr[i][j]));
      obj[arr[i][j]] = obj[arr[i][j]] + 1 || 1;
    }
  }
  const answer = Array.from(set).sort((a, b) => obj[b] - obj[a]);
  return answer;
}

const s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";
console.log(solution(s));
// const arr = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4];
// console.log(bisectLeft(arr, 4));
// console.log(bisectRight(arr, 4));
