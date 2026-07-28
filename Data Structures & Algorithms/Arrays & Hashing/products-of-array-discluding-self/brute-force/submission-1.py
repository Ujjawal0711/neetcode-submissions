# Product of Array Except Self — Method 2: Brute Force  ❌ too slow for the limits
# -----------------------------------------------------------------------------
# Problem: Return an array where answer[i] = product of all elements EXCEPT
#          nums[i]. Must run in O(n) and without using division.
#
# Idea:    The direct reading of the problem — for every index i, loop the whole
#          array again and multiply everything except position i. Correct, but
#          it re-scans the array n times, which violates the O(n) requirement.
#
# Time:  O(n^2)   nested loop, full re-scan for every i
# Space: O(1)     extra (excluding the output array)
#
# Kept as the reference/starting point — it's the intuition the prefix-suffix
# solution optimizes. The key realization when moving on: the inner loop keeps
# recomputing the same partial products, so cache them once as prefix and
# suffix arrays instead.
#
# Trade-off: see ../prefix-suffix/ for the O(n) version that actually passes.
# -----------------------------------------------------------------------------
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = []

        for i in range(n):           # for each index i
            product = 1
            for j in range(n):       # loop through whole array again
                if j != i:           # skip current index i itself
                    product *= nums[j]
            answer.append(product)

        return answer
