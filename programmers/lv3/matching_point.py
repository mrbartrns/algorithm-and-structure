import re


def get_base_point(word, page):
    """
    word parsing and counting function
    Args:
        word: word what I want to match
        page:

    Returns:

    """
    ret = re.sub('[^a-z]', '.', page.lower()).split('.')
    ret = list(filter(lambda x: x == word.lower(), ret))
    return len(ret)


def get_current_website(page):
    p = re.compile(r'<meta property="og:url" content="(.*?)"/>')
    ret = p.findall(page)
    return ret  # return first matched object


def get_external_website(page):
    p = re.compile(r'<a href="(.*?)">')
    ret = p.findall(page)
    return ret


def solution(word, pages):
    answer = 0
    max_scores = 0
    addresses = {}
    scores = [0] * len(pages)
    link_scores = [0] * len(pages)
    exist = set()
    # get index of current website
    for i in range(len(pages)):
        page = pages[i]
        current_website = get_current_website(page)[0]
        addresses[current_website] = i
        exist.add(current_website)
        base_score = get_base_point(word, page)
        outer_sites = get_external_website(page)
        scores[i] = base_score
        link_scores[i] = scores[i] / len(outer_sites) if outer_sites else 0

    for i in range(len(pages)):
        page = pages[i]
        outer_sites = get_external_website(page)
        for j in range(len(outer_sites)):
            outer_site = outer_sites[j]
            if outer_site not in exist:
                continue
            scores[addresses[outer_site]] += link_scores[i]

    for i in range(len(scores)):
        if max_scores < scores[i]:
            max_scores = scores[i]
            answer = i
    return answer


if __name__ == "__main__":
    arr = [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
    word = "blind"
    print(solution(word, arr))
