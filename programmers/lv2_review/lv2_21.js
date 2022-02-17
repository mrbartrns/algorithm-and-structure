const obj = {};
const table = [
  ["-", "cpp", "java", "python"],
  ["-", "backend", "frontend"],
  ["-", "junior", "senior"],
  ["-", "chicken", "pizza"],
];

function solution(info, query) {
  backtrack(0, "");
  info.forEach((el) => {
    getSubSeq(0, "", el.split(" "));
  });
  let newQuery = query.map((el) => el.split(" "));
  const answer = [];
  for (const key in obj) {
    obj[key].sort((a, b) => a - b);
  }
  for (let i = 0; i < newQuery.length; i++) {
    let queryset = "";
    const score = parseInt(newQuery[i][newQuery[0].length - 1]);
    for (let j = 0; j < newQuery[0].length; j += 2) {
      queryset += newQuery[i][j];
    }
    answer.push(obj[queryset].length - lowerBound(obj[queryset], score));
  }
  return answer;
}

function backtrack(idx, subString) {
  if (idx === table.length) {
    obj[subString] = [];
    return;
  }
  for (let i = 0; i < table[idx].length; i++) {
    backtrack(idx + 1, subString + table[idx][i]);
  }
}

function getSubSeq(idx, subString, info) {
  if (idx === info.length - 1) {
    obj[subString].push(Number(info[info.length - 1]));
    return;
  }
  getSubSeq(idx + 1, subString + info[idx], info);
  getSubSeq(idx + 1, subString + "-", info);
}

function lowerBound(arr, target) {
  let start = 0;
  let end = arr.length;

  let mid;
  while (start < end) {
    mid = Math.floor((start + end) / 2);
    if (arr[mid] >= target) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return end;
}

function upperBound(arr, target) {
  let start = 0;
  let end = arr.length;
  let mid;
  while (start < end) {
    mid = Math.floor((start + end) / 2);
    if (arr[mid] > target) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return end;
}

const info = [
  "java backend junior pizza 150",
  "python frontend senior chicken 210",
  "python frontend senior chicken 150",
  "cpp backend senior pizza 260",
  "java backend junior chicken 80",
  "python backend senior chicken 50",
];
const query = [
  "java and backend and junior and pizza 100",
  "python and frontend and senior and chicken 200",
  "cpp and - and senior and pizza 250",
  "- and backend and senior and - 150",
  "- and - and - and chicken 100",
  "- and - and - and - 150",
];

console.log(solution(info, query));
