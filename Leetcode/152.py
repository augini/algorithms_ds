# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        mn, mx = 1, 1
        result = max(nums)

        for i in range(0, length):
            tmp = nums[i] * mx
            mx = max(nums[i] * mx, nums[i] * mn, nums[i])
            mn = min(tmp, nums[i] * mn, nums[i])
            result = max(result, mx)
        return result

    def _maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        mn, mx = [1] * length, [1] * length
        result = max(nums)

        for i in range(0, length):
            if nums[i] == 0:
                mn[i], mx[i] = 1, 1
            else:
                if nums[i] > 0:
                    mx[i] = max(mx[i - 1] * nums[i], mx[i])
                    mn[i] = min(mn[i - 1] * nums[i], mn[i])
                elif nums[i] < 0:
                    mx[i] = max(mn[i - 1] * nums[i], mx[i])
                    mn[i] = min(mx[i - 1] * nums[i], mn[i])
                result = max(result, mx[i])

        return result


sample = Solution()
# print(sample.maxProduct([-2, 0, -1]))
print(sample.maxProduct([2, -5, -2, -4, 3]))
