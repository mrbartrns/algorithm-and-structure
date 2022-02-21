function solution(research, n, k) {
  const INF = 987654321;
  let answer = "";
  const dayCounts = [];
  const issueCounts = {};
  const keySet = new Set();
  research.forEach((issue) => {
    const obj = {};
    for (let i = 0; i < issue.length; i++) {
      const c = issue[i];
      if (!obj.hasOwnProperty(c)) {
        obj[c] = 1;
      } else {
        obj[c] += 1;
      }
      keySet.add(c);
    }
    dayCounts.push(obj);
  });
  for (let i = 0; i < research.length - n + 1; i++) {
    const durationCounts = {};
    for (let j = 0; j < n; j++) {
      for (let key of keySet) {
        if (durationCounts.hasOwnProperty(key)) {
          const amount = dayCounts[i + j][key] || 0;
          if (durationCounts[key] && amount >= k) {
            durationCounts[key] += amount;
          } else {
            durationCounts[key] = -INF;
          }
        } else if (j === 0) {
          const amount = dayCounts[i + j][key] || 0;
          if (amount >= k) {
            durationCounts[key] = amount;
          } else {
            durationCounts[key] = -INF;
          }
        } else {
          durationCounts[key] = -INF;
        }
      }
    }
    for (let key of Object.keys(durationCounts)) {
      if (durationCounts[key] >= 2 * n * k) {
        issueCounts[key] = issueCounts[key] + 1 || 1;
      }
    }
  }
  if (isEmpty(issueCounts)) return "None";
  const ret = Object.entries(issueCounts);
  ret.sort((a, b) => {
    if (a[1] > b[1]) {
      return -1;
    }
    if (a[1] < b[1]) {
      return 1;
    }
    if (a[0] < b[0]) {
      return -1;
    } else {
      return 1;
    }
  });
  return ret[0][0];
}
function isEmpty(object) {
  return Object.keys(object).length === 0 && object.constructor === Object;
}
const research = ["yxxy", "xxyyy"];
const n = 2;
const k = 1;
console.log(solution(research, n, k));
