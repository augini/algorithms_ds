# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        length = len(nums)

        for j in range(1, length):
            for i in range(0, j):
                if nums[j] > nums[i]:
                    LIS[j] = max(LIS[i] + 1, LIS[j])

        return max(LIS)


sample = Solution()
print(sample.lengthOfLIS([0, 1, 0, 3, 2, 3]))
