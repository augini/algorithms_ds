from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # O(logn)
        # m
        while len(nums) > k:
            heapq.heappop(nums)  # O(logn)
        return nums[0]


# Time Comlexity O(m*logn)
