# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 1
        length = len(nums)

        for i in range(length):
            num = nums[i]
            jump -= 1
            if num > jump:
                jump = num
            if jump == 0 and i != length - 1:
                return False
        return True


sample = Solution()
# print(sample.canJump([2, 3, 1, 1, 4]))
print(sample.canJump([3, 2, 1, 0, 4]))
