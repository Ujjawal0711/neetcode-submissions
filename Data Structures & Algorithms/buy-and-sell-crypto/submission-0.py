# Best Time to Buy and Sell (Buy and Sell Crypto)
# -----------------------------------------------------------------------------
# Problem: Given daily prices, find the max profit from buying once and selling
#          once on a LATER day. If no profit is possible, return 0.
#
# Idea:    Single pass. Track the lowest price seen so far (best day to have
#          bought). At each day, the best profit if we sold today is
#          price - min_price. Keep the running maximum of that.
#
# Time:  O(n)   one pass over prices
# Space: O(1)   only two scalars tracked
# -----------------------------------------------------------------------------
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')        # cheapest buy price seen so far
        max_profit = 0                  # best profit found so far

        for price in prices:
            # New low -> this becomes the best day to have bought going forward
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today beats our best profit so far
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
