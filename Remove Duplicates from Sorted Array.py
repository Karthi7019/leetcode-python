class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        n = len(nums)
        for k in range(1, n):
           if nums[k] != nums[i]:
                i = i+1
                nums[i] = nums[k]
        return i+1
