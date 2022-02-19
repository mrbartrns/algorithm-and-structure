// 현재 무게가 weight를 초과한다면
function solution(bridge_length, weight, truck_weights) {
  let answer = 0;
  const q = Array(bridge_length).fill(0);
  let currentWeight = 0;
  while (truck_weights.length) {
    const currentTruckWeight = truck_weights[0];
    currentWeight -= q.shift();
    if (currentTruckWeight + currentWeight <= weight) {
      truck_weights.shift();
      currentWeight += currentTruckWeight;
      q.push(currentTruckWeight);
    } else {
      q.push(0);
    }
    answer += 1;
  }
  answer += q.length;

  return answer;
}

const bridge_length = 100;
const weight = 100;
const truck_weights = [10];
console.log(solution(bridge_length, weight, truck_weights));
