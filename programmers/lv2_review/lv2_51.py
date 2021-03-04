# 카카오 압축
# 투 포인터 알고리즘 사용
"""
1. 길이가 1인 모든 단어를 포함하도록 딕셔너리 초기화
2. 만약 어떤 글자가 사전에 존재한다면, 오른쪽 범위를 1 증가시켜 탐색
3. 범위를 증가시켰을 때 존재하지 않는다면, 단어를 사전에 등록 후 right를 -1 감소시킨 값을 출력함
"""


def solution(msg):
    hs = set()
    words = {}
    ans = []
    left, right = 0, 1
    # 딕셔너리 및 해시 초기화
    idx = 27
    for i in range(26):
        words[chr(i + ord("A"))] = i + 1
        hs.add(chr(i + ord("A")))

    while True:
        while right <= len(msg) and msg[left:right] in hs:
            right += 1

        if right <= len(msg) and msg[left:right] not in hs:
            hs.add(msg[left:right])
            words[msg[left:right]] = idx
            idx += 1
            right -= 1
            ans.append(words[msg[left:right]])
            left = right
            right = left + 1
        elif right > len(msg):
            right -= 1
            ans.append(words[msg[left:right]])
            break

    return ans


print(solution("ABABABABABABABAB"))