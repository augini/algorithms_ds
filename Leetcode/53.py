# https://leetcode.com/problems/maximum-subarray/description/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, sm = nums[0], 0

        for num in nums:
            if sm < 0:
                sm = 0
            sm += num
            maxSum = max(maxSum, sm)

        return maxSum
