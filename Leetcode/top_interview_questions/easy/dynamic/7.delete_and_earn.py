from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # store the each digit count in a hashmap
        digit_counts = Counter(nums)

        # remove duplicates from list
        _unique = list(dict.fromkeys(nums))
        
        # sort the list
        _unique = sorted(_unique)

        points = [_unique[0]*digit_counts[_unique[0]]]
        max_p =points[0]
        
        for i in range(1, len(_unique)):
            total = digit_counts[_unique[i]] * _unique[i]

            if _unique[i-1] + 1 == _unique[i]:
                if i <= 1:
                    points.append(total)
                else:
                    points.append(max(points[0:i-1]) + total)
            
            else:
                points.append(points[i-1] + total)
                
            if points[-1] > max_p:
                max_p = points[-1]
            
        return max_p

Sample = Solution()
# print(Sample.deleteAndEarn([2,2,3,4,43,5,45]))
# print(Sample.deleteAndEarn([2,2,3,3,3,4]))
# print(Sample.deleteAndEarn([3,1]))
# print(Sample.deleteAndEarn([1,1,1,2,4,5,5,5,6]))
print(Sample.deleteAndEarn([1,6,3,3,8,4,8,10,1,3]))