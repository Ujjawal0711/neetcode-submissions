# Two Sum II — Input Array Is Sorted
# -----------------------------------------------------------------------------
# Problem: Given a 1-INDEXED array sorted in ascending order, return the indices
#          of the two numbers adding up to target. Must use O(1) extra space
#          (so the hashmap trick from Two Sum is not allowed here).
#
# Idea:    Because the array is sorted, two pointers from both ends can steer
#          the sum. Too big? The only way to shrink is to move `right` left.
#          Too small? Move `left` right. Each step rules out a whole row of
#          pairs, so one pass is enough.
#
# Time:  O(n)   pointers only ever move toward each other
# Space: O(1)   no extra structures — this is the point of the problem
#
# Why sorting is what makes this work: the sum moves predictably. In an unsorted
# array, moving a pointer tells you nothing about the new sum — which is exactly
# why plain Two Sum needs a hashmap instead. Compare with
# ../../Arrays & Hashing/two-integer-sum/.
#
# Note the `+1` on both returns — the problem is 1-indexed, not 0-indexed.
# -----------------------------------------------------------------------------
class Solution:
    def twoSum(self,numbers,target):
        left = 0
        right = len(numbers)-1
        while left<right:
            if (numbers[left] + numbers[right] == target):
                return [left+1 , right+1]      # +1: answer is 1-indexed
            elif (numbers[left] + numbers[right] > target):
                right -=1                      # sum too big -> shrink from the right
            else:
                left +=1                       # sum too small -> grow from the left
