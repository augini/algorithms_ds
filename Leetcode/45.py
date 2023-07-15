# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums) - 1
        jump = -1
        longest = 0
        step = 0
        i = 0

        while longest < length:
            if i > jump:
                step += 1
                jump = longest
            longest = max(longest, nums[i] + i)
            i += 1
        return step


sample = Solution()
print(sample.jump([1, 1, 1, 1]))
# print(sample.jump([2, 3, 1]))
