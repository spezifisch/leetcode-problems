class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        mins = []
        maxs = []
        for i in range(len_prices):
            price = prices[i]

            prev = i - 1
            if prev < 0:
                prev = i

            post = i + 1
            if post >= len_prices:
                post = i

            if prices[prev] >= price < prices[post]:
                mins.append([i, price])

            if prices[prev] <= price >= prices[post]:
                maxs.append([i, price])

        max_profit = 0
        for min_i, min_price in mins:
            for max_i, max_price in maxs:
                if min_i >= max_i:
                    continue

                profit = max_price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# Runtime: 56 ms, faster than 28.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15.6 MB, less than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
