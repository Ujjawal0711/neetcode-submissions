# Longest Substring Without Repeating Characters
# -----------------------------------------------------------------------------
# Problem: Return the length of the longest substring of s containing no
#          repeated characters. Substring = contiguous, unlike a subsequence.
#
# Idea:    Classic variable-size sliding window. `right` expands the window one
#          character at a time; the set holds exactly what's inside the window.
#          When the incoming char is already present, shrink from the left until
#          the duplicate is gone — then the window is clean again and its size
#          is a candidate answer.
#
# Time:  O(n)              each char is added and removed at most once
# Space: O(min(n, m))      m = charset size; the set holds one window's worth
#
# Why the inner while doesn't make this O(n^2): `left` only ever moves forward,
# never resets. Across the entire run it advances at most n times total, so the
# two pointers together do ~2n work — not n per outer step.
#
# The window is [left, right] inclusive on both ends, which is why its length
# is right - left + 1 rather than right - left.
# -----------------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):

        left = 0
        maxseq = 0
        seen = set()   # same set object throughout -- shrinks/grows in place, never rebuilt

        for right in range(0, len(s)):   # expand window one char at a time
            while (s[right] in seen):
                # duplicate found -- shrink from left, one char at a time,
                # until s[right] is no longer in the window
                seen.remove(s[left])
                left += 1
            # window is now clean -- safe to add current char
            seen.add(s[right])
            # right - left + 1 = count of chars currently in window (inclusive both ends)
            maxseq = max(maxseq, right - left + 1)
        return maxseq
