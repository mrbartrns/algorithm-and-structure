# 회문인지 아닌지 먼저 판별하기
def check_palindrome(text, m):
    begin = 0
    mid = m // 2
    matched = 0
    while begin + m <= len(text):
        left = text[begin: mid + begin]
        right = text[begin + mid: begin + m] if m % 2 == 0 else text[begin + mid + 1: begin + m]
        for i in range(mid):
            if left[i] == right[-1 -i]:
                matched += 1
                if matched == mid:
                    return [1, begin]
            else:
                break
        begin += 1
    return [0, begin]


# print(get_palindrome('abcbaabcba'))
def search(arr, m):
    # 가로로 탐색
    for i in range(len(arr)):
        flag = check_palindrome(arr[i], m)
        if flag[0] == 1:
            return arr[i][flag[1]: flag[1] + m]

    # 세로로 탐색
    for j in range(len(arr[0])):
        text = ''
        for i in range(len(arr)):
            text += arr[i][j]
        flag = check_palindrome(text, m)
        if flag[0] == 1:
            return text[flag[1]: flag[1] + m]

# t = int(input())
# for i in range(t):
#     arr = []
#     n, m = map(int, input().split())
#     for j in range(n):
#         text = input()
#         arr.append(text)
#     print(f'#{i + 1} {search(arr, m)}')

# print(check_palindrome('JAEZNNZEAJ', 10))
# print(search(['ECFQBKSYBBOSZQSFBXKI', 'VBOAIDLYEXYMNGLLIOPP', 'AIZMTVJBZAWSJEIGAKWB', 'CABLQKMRFNBINNZSOGNT', 'NQLMHYUMBOCSZWIOBINM', 'QJZQPSOMNQELBPLVXNRN', 'RHMDWPBHDAMWROUFTPYH',
#     'FNERUGIFZNLJSSATGFHF', 'TUIAXPMHFKDLQLNYQBPW', 'OPIRADJURRDLTDKZGOGA', 'JHYXHBQTLMMHOOOHMMLT', 'XXCNJGTXXKUCVOUYNXZR', 'RMWTQQFHZUIGCJBASNOX', 'CVODFKWMJSGMFTCSLLWO', 'EJISQCXLNQHEIXXZSGKG',
#     'KGVFJLNNBTVXJLFXPOZA', 'YUNDJDSSOPRVSLLHGKGZ', 'OZVTWRYWRFIAIPEYRFFG', 'ERAPUWPSHHKSWCTBAPXR', 'FIKQJTQDYLGMMWMEGRUZ']))
# print(search(['JHYXHBQTLMMHOOOHMMLT'], 13))
print(search(['abcab', 'bbcdd', 'cabcc', 'bcdac', 'abcde'], 3))