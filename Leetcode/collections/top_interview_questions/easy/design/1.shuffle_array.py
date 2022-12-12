class Solution:

    def __init__(self, nums: list[int]):
        self.original = nums
        self.nums = nums

    def reset(self) -> list[int]:
        self.nums = self.original
        return self.nums
        

    def shuffle(self) -> list[int]:
       return 'hey there people'
        


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
param_1 = obj.reset()
param_2 = obj.shuffle()