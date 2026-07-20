# Valid Palindrome
# -----------------------------------------------------------------------------
# Problem: Return True if s reads the same forwards and backwards, considering
#          only alphanumeric characters and ignoring case.
#
# Idea:    Two pointers from both ends moving inward. Skip any non-alphanumeric
#          character, then compare the two characters case-insensitively. A
#          single mismatch means it's not a palindrome.
#
# Time:  O(n)   each pointer crosses the string at most once
# Space: O(1)   in place, no extra copy of the string
# -----------------------------------------------------------------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0                        # pointer starting at the front
        right = len(s) - 1              # pointer starting at the back

        while left < right:
            # Skip non-alphanumeric chars from the left (spaces, punctuation, ...)
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric chars from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the two valid chars, case-insensitively
            if s[left].lower() != s[right].lower():
                return False

            left += 1                   # move both pointers inward and continue
            right -= 1

        return True
