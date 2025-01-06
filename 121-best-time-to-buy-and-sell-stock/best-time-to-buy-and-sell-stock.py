class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = (prices[0], 0) 
        maxProfit = 0
        
        for i, current_price in enumerate(prices):
            if current_price < cheapest[0]:
                cheapest = (current_price, i)

            profit =  current_price - cheapest[0]
            if profit > maxProfit and i > cheapest[1]:
                maxProfit = profit 


        return maxProfit