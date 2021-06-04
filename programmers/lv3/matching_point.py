# 매칭 점수
import re


def get_base_point(word, page):
    p = re.compile(rf"[^a-zA-Z]({word})[^a-zA-Z]|\b({word})\b|\b({word})[^a-zA-Z]|[^a-zA-Z]({word})\b", re.IGNORECASE)
    ret = p.findall(page)
    return len(ret)


def get_current_website(page):
    p = re.compile(r'<meta property="og:url" content="(.+)"/>')
    ret = p.search(page)
    return ret.group(1)  # return first matched object


def get_external_website(page):
    p = re.compile(r'<a href="(.+)"\s|<a href="(.+)"')
    ret = p.findall(page)
    print(ret)
    return ret


def get_score(word, page):
    score = 0
    base_score = get_base_point(word, page)
    external_sites = get_external_website(page)
    score += base_score
    score /= len(external_sites)
    return score


def solution(word, pages):
    answer = 0
    max_scores = 0
    addresses = {}
    scores = [0] * len(pages)
    link_scores = [0] * len(pages)
    exist = set()
    for i in range(len(pages)):
        page = pages[i]
        current_website = get_current_website(page)
        addresses[current_website] = i
        link_scores[i] = get_score(word, page)
        exist.add(current_website)
    for i in range(len(pages)):
        page = pages[i]
        external_sites = get_external_website(page)
        score = link_scores[i]
        scores[i] += score
        for site in external_sites:
            if site not in exist:
                continue
            idx = addresses[site]
            scores[idx] += score
    for i in range(len(scores)):
        if max_scores < scores[i]:
            answer = i
            max_scores = scores[i]
    return answer


if __name__ == "__main__":
    string = "hi hi1234 023hi HI"
    word = "hi"
    p = re.compile(rf"\b({word})\b|[^a-zA-Z]({word})[^a-zA-Z]|\b({word})[^a-zA-Z]|[^a-zA-Z]({word})\b", re.I | re.S)
    print(p.findall(string))