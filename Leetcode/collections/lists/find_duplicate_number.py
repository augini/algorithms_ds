# https://leetcode.com/problems/find-the-duplicate-number/submissions/

from collections import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i + 1 > nums[i]:
                return nums[i]
