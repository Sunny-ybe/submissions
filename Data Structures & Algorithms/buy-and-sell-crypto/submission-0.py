class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profitmax = 0
        minprice = prices[0]
        for i in range(len(prices)):
            profit = prices[i]-minprice
            profitmax = max(profit, profitmax)
            if prices[i] < minprice:
                minprice = prices[i]
            
            

        return profitmax

            


            
        return profitmax
        
        

        