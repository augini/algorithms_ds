class Solution:
    def maxArea(self, height: list[int]) -> int:
       start, end = 0, len(height)-1

       
       max_area = 0
       while start != end:
          shorter = height[start] if height[start] < height[end] else height[end]
          area = (end - start) * shorter
          if area > max_area:
             max_area = area
             
          if height[start] < height[end]:
             start = start+1
          else:
             end = end - 1
         
       return max_area
     
Sample = Solution()
print(Sample.maxArea([1,1]))