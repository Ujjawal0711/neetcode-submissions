class Solution(object):
    def twoSum(Seen, nums, target):
        Seen={}
        for i, num in enumerate(nums):
            missing=target - num
            
            if missing in Seen:
                return [Seen[missing],i]
            Seen[num] = i
        return False