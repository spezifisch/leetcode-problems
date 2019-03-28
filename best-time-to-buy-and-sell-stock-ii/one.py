class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        can_buy = True
        for i in range(len(prices)):
            price = prices[i]
            prev = max(0, i - 1)
            post = min(len(prices) - 1, i + 1)
            if can_buy:
                if prices[prev] >= price < prices[post]:
                    profit -= price
                    can_buy = False
            else:
                if prices[prev] <= price >= prices[post]:
                    profit += price
                    can_buy = True
                
        return profit

# Runtime: 52 ms, faster than 28.27% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 13.7 MB, less than 5.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.

