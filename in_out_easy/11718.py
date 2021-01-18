# 입력값이 얼마인지 모를 때에는 무한정 입력을 받은 후, except EOFError 처리를 한다
while True:
    try:
        string = input()
        print(string)
    except EOFError:
        break