# https://leetcode.com/problems/sliding-window-median/description/

from typing import List
import bisect

# Option 1

# get the array in the window
# sort it in the first slice
# on every move, remove the previous element and insert the new item on the current index in the sorted array
# return the media from the window


class Solution:
    def getMedian(self, nums: List[int]) -> float:
        length = len(nums)
        half = length // 2

        if length % 2 == 0:
            median = (nums[half] + nums[half - 1]) / 2
        else:
            median = float(nums[half])

        return median

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        temp = []
        median = []

        for i in range(k, len(nums) + 1):
            if len(temp) == 0:
                temp = sorted(nums[i - k : i])
            else:
                temp.remove(nums[i - k - 1])
                bisect.insort(temp, nums[i - 1])

            median.append(self.getMedian(temp))

        return median


sample = Solution()
print(sample.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
