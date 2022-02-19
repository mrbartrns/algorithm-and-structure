// programmers 후보키
const obj = {};
function solution(relation) {
  let answer = 0;
  relation.forEach((el) => {
    getSubseq(0, el, "", "");
  });
  const keys = Object.keys(obj);
  keys.sort((a, b) => {
    return a.length < b.length ? -1 : 1;
  });
  for (let key of keys) {
    if (isUniqueKey(key, relation)) {
      answer += 1;
    }
  }
  return answer;
}

function getSubseq(idx, relationArr, subString, subkey) {
  if (idx === relationArr.length) {
    if (!subkey) return;
    if (!obj.hasOwnProperty(subkey)) {
      obj[subkey] = new Set();
    }
    obj[subkey].add(subString);
    return;
  }
  getSubseq(
    idx + 1,
    relationArr,
    subString + relationArr[idx],
    subkey + String(idx)
  );
  getSubseq(idx + 1, relationArr, subString, subkey);
}

function isUniqueKey(key, relation) {
  for (let i = 0; i < 1 << key.length; i++) {
    let string = "";
    for (let j = 0; j < key.length; j++) {
      if (i & (1 << j)) {
        string += key[j];
      }
    }
    if (!string.length) continue;
    if (obj[string].size === relation.length && string.length < key.length) {
      return false;
    }
  }
  if (obj[key].size < relation.length) {
    return false;
  }
  return true;
}

const relation = [
  ["100", "ryan", "music", "2"],
  ["200", "apeach", "math", "2"],
  ["300", "tube", "computer", "3"],
  ["400", "con", "computer", "4"],
  ["500", "muzi", "music", "3"],
  ["600", "apeach", "music", "2"],
];

console.log(solution(relation));
