# Max Product of Two Digits
# -----------------------------------------------------------------------------
# Problem: Given an integer n, return the largest product obtainable from any
#          two of its digits.
#
# Idea:    Every digit is 0-9, so all of them are non-negative. That means the
#          biggest product always comes from the two LARGEST digits — sort
#          ascending and multiply the last two. No need to compare candidate
#          pairs.
#
# Time:  O(d log d)   d = number of digits (~10 max), so effectively O(1)
# Space: O(d)         the digits list
#
# Why "two largest" is safe here: with arrays that can contain negatives, the
# max product might come from two large NEGATIVE numbers (their product is
# positive). Digits can never be negative, so that case can't arise and the
# simple approach is provably correct.
#
# Assumes n has at least 2 digits and is non-negative — a single-digit n would
# raise IndexError on digits[-2], and a negative n would raise ValueError on
# the '-' sign.
#
# Possible follow-up: skip the sort entirely and track the top two digits in a
# single pass for O(d) time. Irrelevant at d<=10, but it's the answer if an
# interviewer asks to drop the sort.
# -----------------------------------------------------------------------------
class Solution(object):
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]   # split n into individual digits
        digits.sort()                        # ascending order
        return digits[-1] * digits[-2]       # product of two largest digits
