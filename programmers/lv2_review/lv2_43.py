# 영어 끝말잇기
def solution(n, words):
    answer = [0, 0]
    overlap = set()
    for i in range(len(words)):
        if len(words[i]) == 1:
            answer = [i % n + 1, i // n + 1]
            return answer
        if words[i] in overlap:
            answer = [i % n + 1, i // n + 1]
            return answer
        if i > 0 and words[i - 1][-1] != words[i][0]:
            answer = [i % n + 1, i // n + 1]
            return answer
        overlap.add(words[i])
    return answer


n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))