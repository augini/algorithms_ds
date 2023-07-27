# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)

        for i in range(length - 3, -1, -1):
            cost[i] = min(cost[i + 1], cost[i + 2]) + cost[i]

        return min(cost[0], cost[1])
