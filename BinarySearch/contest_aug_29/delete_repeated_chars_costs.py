# https://binarysearch.com/problems/Delete-Repeated-Characters-with-Costs


class Solution:
    def solve(self, s, nums):
        length, cost = len(s), 0

        slow, fast = 0, 1

        while fast < length:
            if s[slow] == s[fast]:
                temp_max = nums[slow]

                while s[slow] == s[fast] and fast < length - 1:

                    fast += 1
                    if nums[fast] > temp_max:
                        temp_max = nums[fast]

                slow = fast
                fast += 1
                cost += temp_max
                temp_max = 0
            else:
                slow = fast
                fast += 1
        print(cost)
        return sum(nums) - cost


sample = Solution()
sample.solve("acc", [0, 1, 0])
