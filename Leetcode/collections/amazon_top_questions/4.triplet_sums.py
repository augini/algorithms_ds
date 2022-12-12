class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
      nums.sort()
      triplets = []
      list_len = len(nums)-1

      for i, value in enumerate(nums):
         if value <= 0:
            
            if i != 0 and value == nums[i-1]:
               continue
               
            left, right = i+1, list_len
            
            while left < right:
               _current, _left, _right = value, nums[left], nums[right]

               _sum = _current + _left + _right
               if _sum == 0:
                  triplets.append([_current, _left, _right])
                  
                  if nums[left] == nums[left+1]:
                     while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                  left = left + 1
               elif _sum > 0:
                  right = right -1
               elif _sum < 0:
                  left = left + 1
         else:
            break

      return triplets

Sample = Solution()
print(Sample.threeSum([-1,0,1,2,-1,-4]))
# print(Sample.threeSum([0,0,0]))
# print(Sample.threeSum([0,0,0,0]))
# print(Sample.threeSum([3,0,-2,-1,1,2]))
# print(Sample.threeSum([-1,0,1,0]))


     