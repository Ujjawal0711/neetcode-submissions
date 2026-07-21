import heapq

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