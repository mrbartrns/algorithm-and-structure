# 다단계 칫솔 판매


def dfs(node, value, index_dict, referral, answer):
    if node == "-" or value == 0:
        return
    idx = index_dict[node]
    answer[idx] += value - value * 10 // 100
    dfs(referral[idx], value * 10 // 100, index_dict, referral, answer)


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    amount = list(map(lambda x: x * 100, amount))
    index_dict = {}
    for i in range(len(enroll)):
        index_dict[enroll[i]] = i

    for i in range(len(seller)):
        dfs(seller[i], amount[i], index_dict, referral, answer)
    return answer


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    print(solution(enroll, referral, seller, amount))