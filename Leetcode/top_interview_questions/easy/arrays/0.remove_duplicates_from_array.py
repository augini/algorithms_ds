class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
      
      counter = 1
      
      first, second = 0, 0
      
      while first < len(nums)-1:
         
         if nums[first] != nums[first+1]:
            nums[counter] = nums[first+1]
            
            second = first
            counter =  counter+1
         
         first = first+1
         
      return counter
     

sample = Solution()

# print(sample.removeDuplicates([1, 1, 2, 3, 4, 5, 5, 6, 6]))
# print(sample.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(sample.removeDuplicates([1,2]))
