# Two Sum (Two Integer Sum)
# -----------------------------------------------------------------------------
# Problem: Given nums and a target, return the indices of the two numbers that
#          add up to target. Exactly one valid answer is assumed.
#
# Idea:    One-pass hashmap. For each number, the value we still "need" is
#          target - num. If we've already seen that complement, we're done;
#          otherwise remember the current number and its index for later.
#
# Time:  O(n)   single pass
# Space: O(n)   the map can hold every number
#
# Note: the first parameter here is named `Seen` instead of the conventional
#       `self`. It still works because Python passes the instance as the first
#       arg, and it's immediately reassigned to {} below. Renaming it to `self`
#       would be the idiomatic fix.
# -----------------------------------------------------------------------------
class Solution(object):
    def twoSum(Seen, nums, target):
        Seen = {}                       # value -> index of numbers seen so far
        for i, num in enumerate(nums):
            missing = target - num      # the complement we need to reach target

            if missing in Seen:         # complement already seen -> answer found
                return [Seen[missing], i]
            Seen[num] = i               # record this number's index for future lookups
        return False                    # no pair found (per constraints, shouldn't happen)
