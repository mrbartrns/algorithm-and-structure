# [카카오] 매칭 점수
import re


def get_external_urls(page):
    p = re.compile('<a href="(.+?)">')
    ret = p.findall(page)
    return ret


def get_current_website(page):
    p = re.compile('<meta property="og:url" content="(.+?)"/>')
    ret = p.findall(page)
    return ret[0]


def get_base_point(word, page):
    page = page.lower()
    page = re.sub("[^a-z]", ".", page)
    page = list(page.split("."))
    page = list(filter(lambda x: x == word.lower(), page))
    return len(page)


def solution(word, pages):
    base_point = [0] * len(pages)
    links = [0] * len(pages)
    scores = [0] * len(pages)
    idxs = {}
    urls = {}
    for i in range(len(pages)):
        page = pages[i]
        base_point[i] = get_base_point(word, page)
        current_url = get_current_website(page)
        external_url = get_external_urls(page)
        links[i] += len(external_url)
        idxs[current_url] = i
        urls[current_url] = external_url
    for url in urls:
        for nxt in urls[url]:
            if nxt in idxs:
                scores[idxs[nxt]] += (
                    (base_point[idxs[url]] / links[idxs[url]])
                    if links[idxs[url]] > 0
                    else 0
                )
    for i in range(len(pages)):
        scores[i] += base_point[i]
    return scores.index(max(scores))


if __name__ == "__main__":
    word = "blind"
    pages = [
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>',
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>',
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>',
    ]
    print(solution(word, pages))