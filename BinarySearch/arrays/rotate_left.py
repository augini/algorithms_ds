# https://binarysearch.com/room/Full-Stack-of-Pancakes-0f984Qn5MB

class Solution:
    def solve(self, nums, k):

        k = k % len(nums)

        for i in range(3):
            # reverse up to k
            if i == 0:
                left, right = 0, k-1
            # reverse from k up to the end of list
            elif i == 1:
                left, right = k, len(nums) - 1
            # reverse from beginning to end
            else:
                left, right = 0, len(nums) - 1

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1

        return nums
