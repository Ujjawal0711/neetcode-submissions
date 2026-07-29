# LC 15 · 3Sum
# -----------------------------------------------------------------------------
# Problem: Find all UNIQUE triplets [a,b,c] in nums where a + b + c == 0. The
#          result must not contain duplicate triplets.
#
# Idea:    Sort first, then fix one number and solve Two Sum II on the rest.
#          For each index i, run two pointers over the remaining subarray
#          looking for a pair summing to -nums[i]. Sorting is what makes both
#          the two-pointer sweep and the duplicate-skipping possible.
#
# Time:  O(n^2)      O(n log n) sort + an O(n) two-pointer sweep per element
# Space: O(1)        extra (ignoring the output and the sort's own space)
#
# The three duplicate guards — this is the whole difficulty of the problem:
#   1. `if i > 0 and nums[i] == nums[i-1]: continue`
#        skips a repeated FIRST number, so the same triplet isn't found twice.
#        The `i > 0` matters — without it, i-1 would wrap to the last element.
#   2/3. After recording a hit, advance past repeated left/right values so the
#        identical triplet isn't appended again from the same i.
# Because the array is sorted, duplicates are always adjacent — which is what
# lets a simple neighbour comparison catch them.
#
# Note: nums.sort() mutates the caller's list in place.
#
# Builds directly on ../two-integer-sum-ii/ — the inner loop IS that problem.
# -----------------------------------------------------------------------------
class Solution:
    def threeSum(self, nums):
        nums.sort()                  # sorted order enables two pointers + dup skipping
        result=[]

        for i in range(len(nums)):
            # guard 1: skip a duplicate first element (i > 0 avoids wrapping to nums[-1])
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1               # search only to the RIGHT of i (no re-use, no repeats)
            right = len(nums)-1

            while (left<right):
                if (nums[left]+nums[right]+ nums[i] == 0):
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # guards 2 & 3: skip repeats so the same triplet isn't re-added
                    while (left < right and nums[left] == nums[left-1]):
                        left += 1
                    while (left < right and nums[right] == nums[right+1]):
                        right -= 1

                elif (nums[left]+nums[right]+ nums[i] > 0 ):
                    right-=1         # sum too big -> shrink from the right
                else:
                    left+=1          # sum too small -> grow from the left

        return result
