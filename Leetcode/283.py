from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        l = len(nums)
        curr = 0

        while i < l:
            if nums[i] == 0:
                i += 1
            else:
                nums[curr] = nums[i]
                curr += 1
                i += 1

        for x in range(curr, l):
            nums[x] = 0
