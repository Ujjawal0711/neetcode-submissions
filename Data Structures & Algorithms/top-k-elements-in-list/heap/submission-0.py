# Top K Frequent Elements — Method 1: Min-Heap
# -----------------------------------------------------------------------------
# Problem: Given nums and an integer k, return the k most frequent elements.
#
# Idea:    Count frequencies in a hashmap, then push (count, num) pairs into a
#          min-heap. Whenever the heap grows past k, pop the smallest count —
#          the least frequent element gets evicted. Whatever survives is the
#          top k. The heap never holds more than k+1 items, which is what keeps
#          this at log k instead of log n per operation.
#
# Time:  O(n log k)   n pushes/pops on a heap capped at size k
# Space: O(n)         freq map + O(k) heap
#
# Trade-off: see ../bucket-sort/ for the O(n) version. The heap approach is
#            slower here, but it's the one that generalizes to streaming data
#            where you can't preallocate buckets.
# -----------------------------------------------------------------------------
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
