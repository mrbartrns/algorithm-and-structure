function solution(str1, str2) {
  const str1Arr = divide(str1.toUpperCase());
  const str2Arr = divide(str2.toUpperCase());
  const obj1 = {};
  const obj2 = {};
  for (let i = 0; i < str1Arr.length; i++) {
    obj1[str1Arr[i]] = obj1.hasOwnProperty(str1Arr[i])
      ? obj1[str1Arr[i]] + 1
      : 1;
  }
  for (let i = 0; i < str2Arr.length; i++) {
    obj2[str2Arr[i]] = obj2.hasOwnProperty(str2Arr[i])
      ? obj2[str2Arr[i]] + 1
      : 1;
  }
  let union = 0;
  let intersection = 0;
  const visited = new Set();
  for (const key in obj1) {
    if (visited.has(key)) continue;
    visited.add(key);
    union += Math.max(obj1[key], obj2[key] || 0);
    intersection += Math.min(obj1[key], obj2[key] || 0);
  }
  for (const key in obj2) {
    if (visited.has(key)) continue;
    visited.add(key);
    union += Math.max(obj2[key], obj1[key] || 0);
    intersection += Math.min(obj2[key], obj1[key] || 0);
  }
  return Math.floor((union > 0 ? intersection / union : 1) * 65536);
}

function divide(str) {
  const ret = [];
  for (let i = 0; i < str.length - 1; i++) {
    const sub = str.substring(i, i + 2);
    let flag = true;
    for (let i = 0; i < 2; i++) {
      const c = sub[i];
      if (c < "A" || c > "Z") {
        flag = false;
        break;
      }
    }
    if (flag) {
      ret.push(sub);
    }
  }
  return ret;
}

const str1 = "E=M*C^2";
const str2 = "e=m*c^2";
console.log(solution(str1, str2));
