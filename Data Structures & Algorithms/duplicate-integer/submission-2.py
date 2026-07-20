# Contains Duplicate (Duplicate Integer)
# -----------------------------------------------------------------------------
# Problem: Return True if any value appears at least twice in nums, else False.
#
# Idea:    Walk the list and remember every number in a set. The moment we see a
#          number already in the set, we've found a duplicate. A set gives O(1)
#          average membership checks.
#
# Time:  O(n)   one pass
# Space: O(n)   the set can hold every number
# -----------------------------------------------------------------------------
class Solution(object):
    def hasDuplicate(self, nums):

        hashset = set()                 # numbers seen so far

        for n in nums:
            if n in hashset:            # already seen -> duplicate found
                return True
            hashset.add(n)              # first time seeing n -> record it
        return False                    # finished without any repeat
