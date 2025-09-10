class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos = pos+1
        while pos < len(nums):
            nums[pos] = 0
            pos = pos+1
