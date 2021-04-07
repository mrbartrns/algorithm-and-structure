# 베스트 앨범
def solution(genres, plays):
    answer = []
    gen = {}
    ids = {}
    for i in range(len(genres)):
        gen[genres[i]] = gen.get(genres[i], 0) + plays[i]
        ids[genres[i]] = ids.get(genres[i], []) + [i]

    items = list(gen.items())
    items.sort(key=lambda x: -x[1])

    for key in ids.keys():
        ids[key].sort(key=lambda x: (plays[x], -x))

    for key, _ in items:
        cnt = 0
        while ids[key] and cnt < 2:
            v = ids[key].pop()
            answer.append(v)
            cnt += 1
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 2500, 150, 800, 2500]
print(solution(genres, plays))