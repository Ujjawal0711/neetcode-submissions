class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = []

        for i in range(n):           # for each index i
            product = 1
            for j in range(n):       # loop through whole array again
                if j != i:           # skip current index i itself
                    product *= nums[j]
            answer.append(product)

        return answer

# Time: O(n^2) -- nested loop, full re-scan for every i
# Space: O(1) extra (excluding output array)
# Fails optimal constraint (problem requires O(n), no division)