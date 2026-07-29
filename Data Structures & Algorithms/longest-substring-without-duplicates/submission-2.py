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

# Time: O(n) -- each char added/removed from set at most once
# Space: O(min(n, charset size))