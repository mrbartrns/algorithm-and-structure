class Solution:
    INF = 987654321

    def __init__(self) -> None:
        self.max_length = 0
        self.cache = [self.INF] * 1000
        self.cost = []

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        answer = self.INF
        self.max_length = len(cost)
        self.cost = cost
        answer = self._climb(0)
        self._memset(self.cache, self.INF)
        answer = min(answer, self._climb(1))
        return answer

    def _climb(self, idx):
        if idx == self.max_length:
            return 0
        if idx > self.max_length:
            return self.INF
        if self.cache[idx] < self.INF:
            return self.cache[idx]
        self.cache[idx] = self.cost[idx] + self._climb(idx + 1)
        self.cache[idx] = min(self.cache[idx], self.cost[idx] + self._climb(idx + 2))
        return self.cache[idx]

    @staticmethod
    def _memset(arr, value):
        for i in range(len(arr)):
            arr[i] = value


if __name__ == "__main__":
    a = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    answer = a.minCostClimbingStairs(cost)
    print(answer)
