import math
class Solution:
    def solve(self, hour, minutes):
      angle_minute = minutes * 6 
      angle_hour = (hour % 12) * 30 + (minutes * 0.5)
      
      diff1 = abs(angle_hour - angle_minute)
      diff2 = 360 - diff1
      
      result = diff1 if diff1 < diff2 else diff2
      
      return math.floor(result)
     
sample = Solution()
# print(sample.solve(19, 53))
print(sample.solve(23, 7))
