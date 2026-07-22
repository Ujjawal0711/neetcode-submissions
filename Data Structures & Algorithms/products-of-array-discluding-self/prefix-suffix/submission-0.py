# Product of Array Except Self — Method 1: Prefix & Suffix Products  ⭐ optimal
# -----------------------------------------------------------------------------
# Problem: Return an array where answer[i] = product of all elements EXCEPT
#          nums[i]. Must run in O(n) and without using division.
#
# Idea:    Everything except nums[i] = (everything to its left) × (everything to
#          its right). So precompute two arrays — prefix[i] holds the product of
#          all elements before i, suffix[i] the product of all after i — then
#          multiply them pairwise. Division is never needed, and each array is
#          built in a single pass.
#
# Time:  O(n)   three separate linear passes
# Space: O(n)   prefix + suffix arrays
#
# The off-by-one that's easy to get wrong: prefix[i] uses nums[i-1] (not
# nums[i]) and suffix[i] uses nums[i+1] — because each must EXCLUDE nums[i]
# itself. Also the suffix loop must run backward; a forward range won't work.
#
# Possible follow-up: this can be reduced to O(1) extra space by writing the
# prefix products straight into the answer array, then sweeping right-to-left
# with a single running suffix variable.
#
# Trade-off: see ../brute-force/ for the naive O(n^2) version.
# -----------------------------------------------------------------------------
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1]*n   # prefix[i] = product of everything BEFORE i (whole array, not "half")
        suffix = [1]*n   # suffix[i] = product of everything AFTER i

        # build prefix left -> right
        # use nums[i-1], NOT nums[i] -- prefix[i] must exclude nums[i] itself
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # build suffix right -> left (must go backward, not range(1,n))
        # use nums[i+1], NOT nums[i] -- suffix[i] must exclude nums[i] itself
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        # combine: answer[i] = everything left of i * everything right of i
        # must build a list here (append), not overwrite a single variable each loop
        answer = []
        for i in range(n):
            answer.append(prefix[i] * suffix[i])

        return answer
