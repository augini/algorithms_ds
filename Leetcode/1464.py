# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
from typing import List
import heapq


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        max1 = heapq.heappop(max_heap)
        max2 = heapq.heappop(max_heap)
        return ((max1 * -1) - 1) * ((max2 * -1) - 1)
