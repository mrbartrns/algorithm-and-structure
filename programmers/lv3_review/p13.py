import sys

sys.setrecursionlimit(100000)


def solution(enroll, referral, seller, amount):
    idx_dict = {}
    values = [0] * len(enroll)
    for i in range(len(enroll)):
        idx_dict[enroll[i]] = i
    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100, referral, values, idx_dict)

    return values


def dfs(name, cost, referral, values, idx_dict):
    idx = idx_dict[name]
    nxt = referral[idx]
    value = cost - cost // 10
    values[idx] += value
    if nxt != "-" and cost // 10 > 0:
        dfs(nxt, cost // 10, referral, values, idx_dict)


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["sam", "emily", "jaimie", "edward"]
    amount = [2, 3, 5, 4]
    print(solution(enroll, referral, seller, amount))
