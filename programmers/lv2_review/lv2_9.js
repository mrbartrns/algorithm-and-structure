function solution(orders, course) {
  const answer = [];
  const maxValues = [];
  for (let i = 0; i < 11; i++) {
    maxValues.push(0);
  }
  const seq = {};
  for (let i = 0; i < orders.length; i++) {
    const temp = orders[i].split("");
    temp.sort();
    getSubsequence(temp, "", 0, seq);
  }
  for (const key in seq) {
    maxValues[key.length] = Math.max(maxValues[key.length], seq[key]);
  }

  for (let i = 0; i < course.length; i++) {
    for (const key in seq) {
      if (key.length !== course[i]) continue;
      if (seq[key] === maxValues[course[i]] && maxValues[course[i]] > 1) {
        answer.push(key);
      }
    }
  }

  answer.sort();

  return answer;
}

function getSubsequence(string, subString, idx, seq) {
  if (idx === string.length) {
    if (!subString) return;
    if (seq.hasOwnProperty(subString)) {
      seq[subString] += 1;
    } else {
      seq[subString] = 1;
    }
    return;
  }
  getSubsequence(string, subString + string[idx], idx + 1, seq);
  getSubsequence(string, subString, idx + 1, seq);
}

const orders = ["XYZ", "XWY", "WXA"];
const course = [2, 3, 4];
console.log(solution(orders, course));
