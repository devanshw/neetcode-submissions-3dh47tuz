class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                profit = sell - buy 
                max_profit = max(max_profit, profit)
        return max_profit
        
'''
brute force check every combination and compare sum

prices = [10,1,5,6,7,1]
buy on day 1 then sell on day 2 
loss of 9 
buy low sell high 
if we see a smaller value next day why not buy lower 
if next is smaller - buy = next 
if next is bigger - sell and track max 
'''
        