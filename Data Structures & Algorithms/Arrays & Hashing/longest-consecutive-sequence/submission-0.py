# LC 128 · Longest Consecutive Sequence
# -----------------------------------------------------------------------------
# Problem: Given an unsorted array, return the length of the longest run of
#          consecutive integers (e.g. [100,4,200,1,3,2] -> 4, for 1,2,3,4).
#          Must run in O(n), so sorting is off the table.
#
# Idea:    Dump everything into a set for O(1) lookups, then only start counting
#          from numbers that BEGIN a sequence — i.e. where num-1 is absent. From
#          each true start, walk forward while num+length exists.
#
# Time:  O(n)   see note below — the inner while does NOT make this O(n^2)
# Space: O(n)   the hashset
#
# Why this is O(n) despite the nested loop: the inner while only ever runs for
# numbers that are sequence STARTS. Every other number is skipped instantly by
# the `num - 1 not in num_set` guard. So across the whole run, each number is
# visited by the inner loop at most once — one walk per sequence, not per
# element. Dropping that guard is what would make it O(n^2).
#
# The set also dedups for free, so repeated values can't inflate the count.
# -----------------------------------------------------------------------------
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)   # O(1) lookups, also dedups
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:   # only start if this is a sequence start
                length = 1
                while (num + length) in num_set:   # expand forward only
                    length += 1
                longest = max(longest, length)

        return longest
