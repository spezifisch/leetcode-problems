class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        mins = []
        max_profit = 0
        for i in range(len_prices):
            price = prices[i]
            
            prev = i - 1
            if prev < 0:
                prev = i
                
            post = i + 1
            if post >= len_prices:
                post = i
                
            if prices[prev] >= price < prices[post]:
                mins.append(price)

            if prices[prev] <= price >= prices[post] and mins:
                possible_profits = [price - buy_price for buy_price in mins]
                profit = max(possible_profits)
                if profit > max_profit:
                    max_profit = profit

        return max_profit
    
# Runtime: 56 ms, faster than 28.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.1 MB, less than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock.

