# https://leetcode.com/problems/maximum-ice-cream-bars/description/

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counter = 0

        i = 0
        while coins > 0 and i < len(costs):
            if coins - costs[i] >= 0:
                coins -= costs[i]
                counter += 1
            i += 1

        return counter
