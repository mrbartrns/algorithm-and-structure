function solution(w, h) {
  const gcd = (a, b) => {
    return b === 0 ? a : gcd(b, a % b);
  };
  return w * h - (w + h - gcd(w, h));
}

console.log(solution(100000000, 99999999));
