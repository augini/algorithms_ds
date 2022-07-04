class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
      queue = [0]
      indexes = []
      
      first, end = 0, -1
      
      for ind, val in enumerate(multipliers):
         # print(queue)
         while len(queue) <= 2**ind:
            _current = queue.pop(0)
            
            result = _current + (val * nums[first])
            # indexes.append(f"{_current, val, nums[first]}")
            queue.append(result)
            
            result = _current + (val * nums[end])
            indexes.append(f"{_current, val, nums[end]}")
            queue.append(result)
         
         if ind % 2 == 0:
            first = first+1
            end = end -1
            
      # print(first, end)
      # print(indexes)
       
      return max(queue)

sample = Solution()
# print(sample.maximumScore([1,2,3], [3,2,1]))
print(sample.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))