# 매칭 점수
"""
1. 각 홈페이지에 대해 외부 링크 수 구하기
2. 인덱스로 나타내야 하기 때문에 리스트로 나타내기
3. 외부 점수는 현재 링크가 외부에 사용된 만큼임
"""
import heapq
import re


def solution(word, pages):
    q = []
    external_links = []
    current_links = {}
    base_scores = [0] * len(pages)
    external_points = [0] * len(pages)
    s = set()

    for i in range(len(pages)):
        current_link = get_current_link(pages[i])
        current_links[current_link] = i
        s.add(current_link)
        links = get_external_links(pages[i])
        external_links.append(links)
        base_scores[i] = get_base_point(word, pages[i])

    for i in range(len(pages)):
        for j in range(len(external_links[i])):
            if external_links[i][j] not in s:
                continue
            external_idx = current_links[external_links[i][j]]
            # 외부 링크에 현재 링크 점수를 더함
            external_points[external_idx] += base_scores[i] / len(external_links[i]) if external_links[i] else 0

    for i in range(len(pages)):
        heapq.heappush(q, (-(external_points[i] + base_scores[i]), i))
    return heapq.heappop(q)[1]


def get_external_links(page):
    p = re.compile('<a href="(.+)">')
    ret = p.findall(page)
    return ret


def get_current_link(page):
    p = re.compile('<meta property="og:url" content="(.*?)"/>')
    ret = p.findall(page)
    return ret[0]


def get_base_point(word, page):
    ret = re.sub('[^a-z]', '.', page.lower()).split(".")
    ret = list(filter(lambda x: x == word.lower(), ret))
    return len(ret)


if __name__ == "__main__":
    word = "Muzi"
    pages = [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
    print(solution(word, pages))
