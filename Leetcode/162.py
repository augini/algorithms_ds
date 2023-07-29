# https://leetcode.com/problems/find-peak-element/description/
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        low, high = 0, length - 1

        if length <= 1:
            return 0

        while low < high:
            mid = (low + high) // 2

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        if low == high and nums[high] > nums[high - 1]:
            return low

        return -1

    def _findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        low, high = 0, length - 1

        if length <= 1:
            return 0

        while low <= high:
            mid = (low + high) // 2

            if mid < length - 1 and nums[mid] < nums[mid + 1]:
                low = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                high = mid - 1
            else:
                return mid


sample = Solution()
print(sample.findPeakElement([1, 2]))
