# LC 11 · Container With Most Water
# -----------------------------------------------------------------------------
# Problem: Each element is a vertical line's height. Pick two lines that, with
#          the x-axis, hold the most water. Area = width × the SHORTER of the
#          two heights (water spills over the shorter side).
#
# Idea:    Start at the widest possible container (both ends) and always move
#          the pointer at the SHORTER line inward. Width shrinks with every
#          step, so the only way to beat the current area is to find a taller
#          line — and the shorter side is what caps the height.
#
# Time:  O(n)   single pass, pointers converge
# Space: O(1)
#
# Why moving the shorter side is safe (the key insight): the area is capped by
# the shorter line. Moving the TALLER pointer inward loses width while the
# height stays capped by that same short line, so the area can never improve.
# Moving the shorter one is the only move with any upside — so nothing is missed.
# -----------------------------------------------------------------------------
class Solution:
    def maxArea(self, heights):
        left = 0
        right = len(heights)-1
        maxarea= 0
        area = 0

        while (left < right):
            # shorter line caps the height; (right - left) is the width
            area = min(heights[left] , heights[right]) * (right - left)

            if(heights[left] < heights[right]):
                left += 1                       # move the shorter side inward
            else:
                right -= 1

            maxarea = max(maxarea , area)

        return maxarea
