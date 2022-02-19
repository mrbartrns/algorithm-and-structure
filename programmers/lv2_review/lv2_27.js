function solution(citations) {
  let answer = 0;
  citations.sort((a, b) => a - b);
  let start = 0;
  let end = citations.length - 1;
  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    let h = citations.length - mid;
    if (citations[mid] >= h && h >= citations.length - h) {
      answer = h;
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return answer;
}

const citations = [3, 0, 6, 1, 5];
console.log(solution(citations));
