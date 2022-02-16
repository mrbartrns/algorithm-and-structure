function solution(record) {
  const answer = [];
  const userList = {};
  for (let i = 0; i < record.length; i++) {
    const [op, id, nickname] = record[i].split(" ");
    if (op === "Enter") {
      userList[id] = nickname;
    } else if (op === "Change") {
      userList[id] = nickname;
    }
  }
  for (let i = 0; i < record.length; i++) {
    const [op, id, nickname] = record[i].split(" ");
    if (op === "Enter") {
      answer.push(`${userList[id]}님이 들어왔습니다.`);
    } else if (op === "Leave") {
      answer.push(`${userList[id]}님이 나갔습니다.`);
    }
  }
  return answer;
}

const record = [
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
];
console.log(solution(record));
