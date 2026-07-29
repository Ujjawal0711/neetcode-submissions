# LC 121 · Best Time to Buy and Sell — Method 2: Sliding Window (two pointers)
# -----------------------------------------------------------------------------
# Problem: Given daily prices, find the max profit from buying once and selling
#          once on a LATER day. If no profit is possible, return 0.
#
# Idea:    Treat it as a window: `left` is the buy day, `right` the sell day.
#          Slide `right` forward computing the profit at each step. Whenever the
#          price at `right` drops below the buy price, that day becomes the new
#          (cheaper) buy day — a better window can only start there.
#
# Time:  O(n)   single pass
# Space: O(1)
#
# Why jumping left straight to right is correct: any later sell day would rather
# buy at this new lower price, so no window starting before it can ever win
# again. This is the same reasoning as tracking a running minimum — see
# ../min-price-tracking/ for that formulation. The two are equivalent; this one
# just frames it explicitly as a window, which is how the rest of the Sliding
# Window problems are set up.
#
# Note: `left = 0` / `right = 1` are assigned up front, but `right` is
# immediately rebound by the for-loop — only `left` actually carries state.
# -----------------------------------------------------------------------------
class Solution:
    def maxProfit(self, prices):
        left = 0
        right = 1
        maxprofit = 0

        for right in range(1 , len(prices)):            #iterating right pointer
            profit = prices[right] - prices[left]       #checking profit according to right
            maxprofit = max(maxprofit , profit)         #updating Maxprofit
            if (prices[right] < prices [left]):         #checking if left(buying price) is greater than right(selling price)
                left = right                            #If yes skip to right directly

        return maxprofit
