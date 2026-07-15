class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest price encountered so far
            if price < min_price:
                min_price = price
            # Calculate profit if sold today, update max_profit if it's a new high
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit