class Solution:
   def threeSumClosest(self, nums: list[int], target: int) -> int:
      nums.sort()
      diff = float('inf')
      
      for i, value in enumerate(nums):
         if i != 0 and value == nums[i-1]:
            continue
            
         left, right = i+1, len(nums)-1
         while left < right:
            _sum = value + nums[left] + nums[right]
            difference = target - _sum
            
            # print(value, nums[left], nums[right], _sum, difference, min_difference)

            # check if initialazing min_difference to target is the right approach
            if abs(difference) <= abs(diff):
               diff = difference
               
            if _sum >= target:
               right = right -1
               
            elif _sum < target:
               left = left + 1

      return target - diff

Sample = Solution()
# print(Sample.threeSumClosest([-1,2,1,-4], 1)) # -4, -1, 1, 2
# print(Sample.threeSumClosest([0,0,0], 1))
# print(Sample.threeSumClosest([1,1,1,1], 0))
# print(Sample.threeSumClosest([0,2,1,-3], 1))
# print(Sample.threeSumClosest([1,1,1,0], 100))
# print(Sample.threeSumClosest([0,2,1,-3], 1)) # -3 0 1 2
# print(Sample.threeSumClosest([1,-3,3,5,4,1], 1)) # -3 1 3 4 5
print(Sample.threeSumClosest([0,-4,1,-5], 0))
