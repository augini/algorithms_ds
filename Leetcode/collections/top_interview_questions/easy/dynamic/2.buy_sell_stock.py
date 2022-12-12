class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        min, max = prices[0], prices[0]
        
        profit = 0
        
        for price in prices:
            if price < min:
                min = price
                max = price
                
            if price > max:
                max = price
                gain = max-min
                
                if gain > profit:
                    profit = gain
                    
        return profit
     

Sample = Solution()
print(Sample.maxProfit([7,6,4,3,1]))