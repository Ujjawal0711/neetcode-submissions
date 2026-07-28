# Valid Anagram
# -----------------------------------------------------------------------------
# Problem: Return True if t is an anagram of s (same characters, same counts).
#
# Idea:    Anagrams must be the same length. Use one tally dict: add 1 for each
#          char of s, subtract 1 for the char at the same index in t. If s and t
#          have identical letter counts, every entry cancels out to 0 at the end.
#
# Time:  O(n)   single pass over both strings, then a pass over the tally
# Space: O(1)   at most 26 distinct lowercase letters (bounded alphabet)
# -----------------------------------------------------------------------------
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):            # different lengths -> can't be anagrams
            return False

        tally = {}                      # char -> running balance (s adds, t subtracts)

        for i in range(len(s)):
            chars = s[i]                # char from s at index i
            chart = t[i]                # char from t at index i

            tally[chars] = tally.get(chars, 0) + 1   # count s's char up
            tally[chart] = tally.get(chart, 0) - 1   # count t's char down

        for count in tally.values():    # every char must net to zero
            if count != 0:
                return False

        return True
