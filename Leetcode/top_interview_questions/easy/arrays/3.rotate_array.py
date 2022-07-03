# first approach, linear time but uses O(n) space
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [0] * len(nums)

        for i,  value in enumerate(nums):
           new_i = (i+k) % len(nums)
           result[new_i] = value
         
        for i,  value in enumerate(result):
           nums[i] = result[i]

# Reference: https://stackoverflow.com/questions/60177936/rotate-array-list-in-linear-time-and-constant-memory

# It is mentioned that there is a pattern to rotate by k steps
# first reverse 0, k elements, then reverse k+1, n elements and reverse the entire list.

# now let's try to come up with constant memory solution
    def rotate_constant_memory(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        for x in range (0, 2):
          # reverse the numbers until length-1-k 
           if x == 0: 
             i = 0
             j = len(nums) - 1 - k
             
          # reverse the numbers from length - k until length
           else:
             i = len(nums) - k
             j = len(nums) - 1
        
           while i < j:
               temp = nums[i]
               nums[i] = nums[j]
               nums[j] = temp
               
               i = i+1
               j = j-1
         
        # reverse the entire array 
        nums.reverse()

Sample = Solution()
# print(Sample.rotate([-1,-100,3,99], 2))
# print(Sample.rotate_constant_memory([-1,-100,3,99], 2))
print(Sample.rotate_constant_memory([1,2,3,4,5,6,7], 3))
# print(Sample.rotate_constant_memory([1,2,3,4,5,6,7,8,9], 3))
# print(Sample.rotate_constant_memory([1,2,3,4,5,6], 11))

[1,2,3,4,5,6,7]    # 7 - 3 = 4 0, length(arrray) - 1 - k
[4, 3, 2, 1, 5, 6, 7] # length(arrray) - k , length(array)
[4, 3, 2, 1, 7, 6, 5] # reverse everything
[5, 6, 7, 1, 2 ,3 ,4]