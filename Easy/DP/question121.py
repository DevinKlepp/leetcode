class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        lowprice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowprice:
                lowprice = prices[i]
            elif prices[i] - lowprice > profit:
                profit = prices[i] - lowprice
        return profit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2):
            return 0
        profit = 0
        purchase = 2**31 - 1
        for i in range(0, len(prices)):
            if prices[i] < purchase:
                purchase = prices[i]
            else:
                profit = max(profit, prices[i] - purchase)
        return profit
            
