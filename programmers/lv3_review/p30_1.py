# 매칭 점수
import re


def solution(word, pages):
    external_urls = []
    current_urls = {}
    base_scores = []
    link_scores = []
    s = set()
    for i in range(len(pages)):
        current_url = get_current_url(pages[i])
        base_score = get_base_score(word, pages[i])
        external_url = get_external_urls(pages[i])
        current_urls[current_url] = i
        base_scores.append(base_score)
        external_urls.append(external_url)
        link_score = base_score / len(external_url) if external_url else 0
        link_scores.append(link_score)
        s.add(current_url)

    for i in range(len(pages)):
        for j in range(len(external_urls[i])):
            if external_urls[i][j] not in s:
                continue
            idx = current_urls[external_urls[i][j]]
            base_scores[idx] += link_scores[i]

    max_score = 0
    answer = 0
    for i in range(len(base_scores)):
        if max_score < base_scores[i]:
            max_score = base_scores[i]
            answer = i
    return answer


def get_external_urls(page):
    p = re.compile('<a href="(.*?)">')
    ret = p.findall(page)
    return ret


def get_current_url(page):
    p = re.compile('<meta property="og:url" content="(.*?)"/>')
    ret = p.findall(page)
    return ret[0]


def get_base_score(word, page):
    ret = re.sub('[^a-z]', '.', page.lower()).split(".")
    ret = list(filter(lambda x: x == word.lower(), ret))
    return len(ret)


if __name__ == "__main__":
    word = "blind"
    pages = [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
    print(solution(word, pages))
