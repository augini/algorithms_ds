# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    right = mid - 1

        return -1

    def _search(self, nums: List[int], target: int) -> int:
        # find the index of the breaking point and re rotate the array
        start, end = 0, len(nums) - 1

        while nums[start] > nums[end]:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        # re rotate
        nums_sorted = [*nums[start : len(nums)], *nums[0:start]]

        # do the binary search in a sorted list
        start, end = 0, len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums_sorted[mid] < target:
                start = mid + 1
            elif nums_sorted[mid] > target:
                end = mid
            else:
                return nums.index(nums_sorted[mid])

        return -1
