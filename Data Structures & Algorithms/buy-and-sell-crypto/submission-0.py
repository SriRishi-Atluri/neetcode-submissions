class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_price = prices[0]
        max_profit = 0 

        for price in prices: 
            if price < curr_price: 
                curr_price = price
            else: 
                profit = price - curr_price 
                max_profit = max (profit,max_profit)
        
        return max_profit