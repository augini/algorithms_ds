# https://binarysearch.com/room/Full-Stack-of-Pancakes-0f984Qn5MB?questionsetIndex=1

class Solution:
    def solve(self, nums):
        length = len(nums) - 1

        for i in range(0, length-1, 4):
            temp = nums[i]
            nums[i] = nums[i+2]
            nums[i+2] = temp
        
        for i in range(1, length-1, 4):
            temp = nums[i]
            nums[i] = nums[i+2]
            nums[i+2] = temp

        return nums
        