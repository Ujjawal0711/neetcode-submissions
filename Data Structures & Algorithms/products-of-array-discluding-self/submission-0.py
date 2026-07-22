class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1]*n   # prefix[i] = product of everything BEFORE i (whole array, not "half")
        suffix = [1]*n   # suffix[i] = product of everything AFTER i

        # build prefix left -> right
        # use nums[i-1], NOT nums[i] -- prefix[i] must exclude nums[i] itself
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # build suffix right -> left (must go backward, not range(1,n))
        # use nums[i+1], NOT nums[i] -- suffix[i] must exclude nums[i] itself
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        # combine: answer[i] = everything left of i * everything right of i
        # must build a list here (append), not overwrite a single variable each loop
        answer = []
        for i in range(n):
            answer.append(prefix[i] * suffix[i])

        return answer