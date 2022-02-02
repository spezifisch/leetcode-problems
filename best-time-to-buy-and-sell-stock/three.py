class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = None
        max_profit = 0
        for price in prices:
            if min_so_far is None or price < min_so_far:
                min_so_far = price
            else:
                profit = price - min_so_far
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# Runtime: 40 ms, faster than 99.01% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.9 MB, less than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
