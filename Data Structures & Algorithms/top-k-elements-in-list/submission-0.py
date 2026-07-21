import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}   # hashmap: num -> frequency count
        heap = []   # min-heap of size k: stores (count, num) pairs

        # Step 1: count frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            # .get(num, 0) -> current count, or 0 if num not seen yet

        # Step 2: maintain a min-heap of the k most frequent nums
        for num, count in freq.items():
            # freq.items() -> (num, count) pairs from hashmap
            heapq.heappush(heap, (count, num))
            # tuple ordered (count, num) so heap sorts by count (frequency)
            if len(heap) > k:
                heapq.heappop(heap)
                # evict smallest count -> keeps only top k frequencies

        # Step 3: extract just the numbers from heap (ignore counts)
        return [num for count, num in heap]

# Time: O(n log k) | Space: O(n) for freq map + O(k) for heap