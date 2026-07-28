class Solution:
    def maxArea(self, heights):
        left = 0 
        right = len(heights)-1
        maxarea= 0
        area = 0

        while (left < right):
            area = min(heights[left] , heights[right]) * (right - left)

            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
            
            maxarea = max(maxarea , area)           

        return maxarea 