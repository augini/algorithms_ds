# https://leetcode.com/problems/koko-eating-bananas/
from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # do a binary search between 0 and the max element in the array
        start, end = 1, max(piles)
        min_k = end

        while start <= end:
            mid = (start + end) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / mid)
            if time > h:
                start = mid + 1
            elif time <= h:
                min_k = mid
                end = mid - 1
        return min_k

        # for every single item, check if it is less than or equal to the given hours
