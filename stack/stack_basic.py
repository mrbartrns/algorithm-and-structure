class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, el):
        self.items.append(el)
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop(-1) # return을 꼭 해줘야 함, 안그러면 값이 안나옴!
        else:
            return
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if len(self.items) != 0:
            return self.items[-1]
        else:
            return
    
    def __repr__(self):
        return str(self.items) # 어떻게 생겨먹었는지 보여주는 메서드


# ex1 stack을 이용하여 괄호 검사 실행
# 소괄호 검사, 중괄호 검사 따로?
'''
str1 = '(((1 + 1) * 1)'
stack = Stack()
for c in str1:
    if c == '(':
        stack.push(c)
    elif c == ')':
        p = stack.pop()

print(stack)

if stack.is_empty() and p is not None:
    print(True)
else:
    print(False)

'''

# memoization 활용
memo = [0, 1]
def fibo_memoization(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo_memoization(n - 1) + fibo_memoization(n - 2)) # 자료를 저장하고 필요할 때 꺼내쓰는 형태가 스택과 유사하다.
    return memo[n]

print(fibo_memoization(3))

# 동적계획법
# 개념: 먼저 입력크기가 작은 부분 문제들을 모두 해결 한 후에, 그 해를 이용하여 보다 큰 크기의 부분문제들을 해결 > 최종적으로 원래 주어진 입력의 문제를 해결
def fibo_dp(n):
    memo = [0, 1]
    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    print(memo)
    return memo[n]

# print(fibo_dp(4))

def factorial_dp(n):
    memo = [1]
    for i in range(1, n + 1):
        memo.append(memo[i - 1] * i)
    print(memo)
    return memo[n]

print(factorial_dp(5))

