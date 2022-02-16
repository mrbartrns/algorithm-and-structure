const INF = 987654321;
function solution(s) {
  if (s.length === 1) return 1;
  let answer = INF;
  const compacted = [];
  for (let jump = 1; jump <= Math.floor(s.length / 2); jump++) {
    let count = 0;
    let prev = null;
    let compactedString = "";
    for (let i = 0; i < s.length; i += jump) {
      let j = i + jump;
      if (!prev) {
        prev = s.substring(i, j);
        count += 1;
      } else if (prev === s.substring(i, j)) {
        count += 1;
      } else {
        compactedString += count > 1 ? String(count) : "";
        compactedString += prev;
        prev = s.substring(i, j);
        count = 1;
      }
    }
    compactedString += count > 1 ? String(count) : "";
    compactedString += prev;
    compacted.push(compactedString);
  }
  for (let i = 0; i < compacted.length; i++) {
    answer = Math.min(answer, compacted[i].length);
  }
  return answer;
}

const s = "a";
console.log(solution(s));
