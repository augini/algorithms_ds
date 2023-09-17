from heapq import heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # 1. initialize max and min heaps
        # 2. make iterations up to k:
        # 2.1 pick the items that require less than current capital from min heap and push to max heap
        # 2.2 pick the items from max heap and add their capital to current running capital

        capital_heap = []  # min heap
        profit_heap = []  # max heap

        for i in range(0, len(capital)):
            heappush(capital_heap, (capital[i], i))

        for i in range(0, k):
            while len(capital_heap) and capital_heap[0][0] <= w:
                heappush(profit_heap, -profits[heappop(capital_heap)[1]])

            w += -heappop(profit_heap)

        return w


sample = Solution()
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]

print(sample.findMaximizedCapital(k, w, profits, capital))
