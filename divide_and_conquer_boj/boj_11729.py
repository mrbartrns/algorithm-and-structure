# BOJ 11729
# 규칙을 파악하는 것이 가장 중요, 그리고 그것을 식으로 표현할 수 있는지?

n = 3  # 탑의 개수

# 카운트 함수와 하노이의 탑을 프린트 하는 결과는 항상 동시에 수행될 필요가 없다
# 하나의 함수로 모든걸 표현해야된다는 강박관념을 버리기
def hanoi(from_, to_, aux_, n):
    if n == 1:
        print(from_, to_)
        return
    # n - 1개를 from_에서 aux_로 보낸다. 식 그대로 이해하는것이 편하다.
    # 이것이 다 실행됬으면 호출 스택을 빠져나와 다 옮겨졌다는 뜻과 같다.
    #  따라서 마지막 n번째 블록이 from_에서 to_로 이동한다.
    hanoi(from_, aux_, to_, n - 1)
    print(from_, to_)
    hanoi(aux_, to_, from_, n - 1)


total = 0
for _ in range(n):
    total *= 2
    total += 1
print(total)
hanoi(1, 3, 2, n)
# 하노이는 총 두번의 재귀함수와 한번의 n번째 블록이 옮겨지므로 2An + 1
