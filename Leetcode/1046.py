# https://leetcode.com/problems/last-stone-weight/description/
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)

            if second > first:
                stones.append(first - second)
                heapq.heapify(stones)

        stones.append(0)
        return -stones[0]
