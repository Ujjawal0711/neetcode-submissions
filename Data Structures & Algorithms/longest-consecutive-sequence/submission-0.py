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

# Time: O(n) -- each number is only ever expanded once (from its true start)
# Space: O(n) -- hashset