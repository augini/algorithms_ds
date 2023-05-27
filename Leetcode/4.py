# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List
from math import floor


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # join those two arrays with pointers
        length = len(nums1) + len(nums2)
        nums = [0] * length
        p1, p2 = 0, 0

        for i in range(length):
            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] <= nums2[p2]:
                    nums[i] = nums1[p1]
                    p1 += 1
                else:
                    nums[i] = nums2[p2]
                    p2 += 1
            elif p1 >= len(nums1):
                nums[i] = nums2[p2]
                p2 += 1
            else:
                nums[i] = nums1[p1]
                p1 += 1

        def get_median(numbers):
            mid = floor(len(numbers) / 2)

            if len(numbers) % 2 == 0:
                return (numbers[mid] + numbers[mid - 1]) / 2
            else:
                return numbers[mid]

        return get_median(nums)
