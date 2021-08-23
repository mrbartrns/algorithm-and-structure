# 직업군 추천하기

def solution(table, languages, preference):
    arr = []
    idx = []
    for row in table:
        scores = {}
        score = 5
        r = row.split(" ")
        for i in range(len(r)):
            if i == 0:
                idx.append(r[i])
            else:
                scores[r[i]] = score
                score -= 1
        arr.append(scores)
    ret = [0] * len(table)
    for i in range(len(table)):
        score = 0
        for j in range(len(languages)):
            language = languages[j]
            pref = preference[j]
            score += arr[i].get(language, 0) * pref
        ret[i] = score

    score = ret[0]
    last_idx = 0
    for i in range(1, len(ret)):
        if score < ret[i]:
            last_idx = i
            score = ret[i]
        elif score == ret[i] and idx[i] < idx[last_idx]:
            last_idx = i

    return idx[last_idx]


if __name__ == '__main__':
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    print(solution(table, languages, preference))
