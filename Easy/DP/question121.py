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
