class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell 
            else:
                profit = prices[sell] - prices[buy] 
                max_profit = max(max_profit, profit)
            sell += 1
        
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
        