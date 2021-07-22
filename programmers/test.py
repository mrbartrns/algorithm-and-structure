import re


def solution(word, pages):
    base_points = []
    external_urls = []
    link_scores = []
    s = set()
    current_urls = {}
    for i in range(len(pages)):
        page = pages[i]
        base_point = get_base_point(word, page)
        base_points.append(base_point)
        external_url = get_external_urls(page)
        external_urls.append(external_url)
        link_scores.append(base_point / len(external_url) if len(external_url) else 0)
        current_url = get_current_url(page)
        current_urls[current_url] = i
        s.add(current_url)

    # 현재 외부링크에 있는 링크가 s에 존재한다면, 외부링크 점수에 현재 링크 점수를 더한다
    for i in range(len(pages)):
        for j in range(len(external_urls[i])):
            if external_urls[i][j] in s:
                cur_url_idx = current_urls[external_urls[i][j]]
                base_points[cur_url_idx] += link_scores[i]

    return base_points.index(max(base_points))


def get_base_point(word, page):
    new_page = re.sub("[^a-z]", ".", page.lower())
    ret = list(filter(lambda x: x == word.lower(), new_page.split(".")))
    return len(ret)


def get_current_url(page):
    p = re.compile('<meta property="og:url" content="(.*?)"/>')
    ret = p.findall(page)
    return ret[0]


def get_external_urls(page):
    p = re.compile('<a href="(.*?)">')
    ret = p.findall(page)
    return ret


if __name__ == "__main__":
    word = "blind"
    pages = [
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>',
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>',
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>',
    ]
    print(solution(word, pages))
