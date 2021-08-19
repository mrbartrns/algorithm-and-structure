"""
총 G판의 프리셀 게임을 했으며 오늘은 D판의 프리셀 게임을 했다.
오늘 한 D판중 Pd퍼센트의 게임을 이겼고 지금까지 한 G판중 Pg퍼센트의 게임을 이겼다.
총 G판의 게임을 한 것은 오늘 한 D판의 게임이 포함된다?

N = 100, Pd = 1, Pg = 50
Pd의 경우
승률이 1이므로 1 과 100 사이의 최대공약수를 찾는다.
100 // 최대공약수의 값이 <= N이면 가능하고, 아니면 가능하지 않다.
100 // 최대공약수의 값의 배수들은 모두 가능하다(N보다 작은)
100 // 최대공약수의 값은 적어도 오늘 했어야 하는 판수이다.

Pg의 경우
승률이 50이므로 50 과 100 사이의 최대공약수를 찾는다. >> 50
100 // 최대공약수의 값이 적어도 총 해야 하는 횟수가 되고, 이것의 배수들은 모두 가능하다.
2, 4, 6, 8, 10 ...
1) Pd의 최대공약수 % Pg의 최대공약수를 나누었을 때 나머지가 0이라면 True
> 50 % 2 == 0

N = 1000, Pd = 81, Pg = 83
100과 81의 최대공약수는 1이고 100 // 1 = 100이므로 100의 배수들은 모두 가능하다. 이는 N보다 작다.
100과 83의 최대공약수는 1이고 100 // 1 = 100이므로 100의 배수들은 모두 가능하다.
Pd % Pg == 0

N = 10, Pd = 10, Pg = 100
100 과 10의 최대공약수는 10이고 100 // 10 = 10이므로 10의 배수들이 가능하다. 이는 N보다 작다.
100과 100의 최대공약수는 100이고 100 // 100 = 1이므로 1의 배수들은 모두 가능하다.


"""
# SWEA 12051 프리셀 통계
import sys

sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def check(n, pd, pg):
    a = gcd(100, pd)
    if a > n:
        return False
    if pg * 2 - pd > 100:
        return False
    return True


t = int(input())
for tc in range(t):
    n, pd, pg = map(int, input().split())
    answer = 'Possible' if check(n, pd, pg) else 'Broken'
    print(f'#{tc + 1} {answer}')
