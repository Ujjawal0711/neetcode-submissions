# Top K Frequent Elements — Method 2: Bucket Sort  ⭐ most optimized
# -----------------------------------------------------------------------------
# Problem: Given nums and an integer k, return the k most frequent elements.
#
# Idea:    Key insight — a frequency can never exceed len(nums). So instead of
#          sorting by frequency, use frequency AS an array index. Build
#          len(nums)+1 buckets where buckets[i] holds every number appearing
#          exactly i times, then walk the buckets from the highest frequency
#          downward and collect until we have k. No sorting, no heap.
#
# Time:  O(n)   count pass + bucket fill + one walk over the buckets
# Space: O(n)   freq map + bucket array
#
# Why buckets are sized len(nums)+1: index 0 is unused (nothing has frequency
# 0) and the max possible frequency is len(nums) when every element is equal,
# so we need indices 0..len(nums) inclusive.
#
# Trade-off: see ../heap/ for the O(n log k) version. Bucket sort wins on speed
#            but needs all the data up front to size the buckets.
# -----------------------------------------------------------------------------
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}   # hashmap: num -> frequency count
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            # .get(num, 0) -> current count, or 0 if unseen

        # bucket index = frequency; bucket[i] holds all nums with freq i
        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in freq.items():
            buckets[count].append(num)
            # placing num directly into its frequency bucket

        result = []
        for i in range(len(buckets)-1, 0, -1):
            # walk buckets from highest freq down to freq=1 (skip index 0)
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    # stop as soon as we have k numbers
