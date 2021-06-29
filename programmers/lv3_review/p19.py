import heapq


def solution(genres, plays):
    ret = []
    genres_q = []
    songs = {}
    counts = {}
    for i in range(len(genres)):
        genre = genres[i]
        cnt = plays[i]
        counts[genre] = counts.get(genre, 0) + cnt
        songs[genre] = songs.get(genre, []) + [(-cnt, i)]

    for key in counts:
        heapq.heappush(genres_q, (-counts[key], key))
        heapq.heapify(songs[key])

    while genres_q:
        _, genre = heapq.heappop(genres_q)
        for _ in range(2):
            if songs[genre]:
                _, idx = heapq.heappop(songs[genre])
                ret.append(idx)
    return ret


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))
