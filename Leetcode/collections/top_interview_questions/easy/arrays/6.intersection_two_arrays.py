class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
                
            elif nums1[i] < nums2[j]:
                while i<len(nums1) and nums1[i] < nums2[j]:
                    i=i+1
                    
            elif nums2[j] < nums1[i]:
                while j < len(nums2) and nums2[j] < nums1[i]:
                    j=j+1
        return result
     

sample = Solution()
# print(sample.intersect([1,2,2,1],[2,2]))
# print(sample.intersect([4,9,5], [9,4,9,8,4]))
print(sample.intersect([1,1], [1,2]))