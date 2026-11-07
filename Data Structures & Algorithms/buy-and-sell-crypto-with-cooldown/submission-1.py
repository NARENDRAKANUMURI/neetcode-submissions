class Solution:
    def maxProfit(self, prices):
        hold = float("-inf")
        sold = 0
        rest = 0

        for price in prices:
            prevSold = sold

            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prevSold)

        return max(sold, rest)