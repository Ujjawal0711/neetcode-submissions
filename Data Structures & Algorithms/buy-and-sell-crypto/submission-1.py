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