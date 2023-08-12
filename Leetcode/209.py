# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # length = len(nums)
        # left, right = 0, 0
        # curr_sum = 0  # Initialize current sum
        # result = float('inf')

        # while right < length:
        #     curr_sum += nums[right]

        #     while curr_sum >= target:
        #         result = min(result, right - left + 1)
        #         curr_sum -= nums[left]
        #         left += 1

        #     right += 1

        # if result == float('inf'):
        #     return 0
        # return result

        result = float("inf")
        total, left = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                result = min(result, i - left + 1)
                total -= nums[left]
                left += 1

        return 0 if result == float("inf") else result


sample = Solution()
print(sample.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
