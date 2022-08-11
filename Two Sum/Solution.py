class Solution(object):
    def twoSum(self, nums, target):
        for ci, i in enumerate(nums):
            diff = target - i
            dlist = nums[ci+1:]
            if diff in dlist:
                return(ci, nums.index(diff) + ci + 1)
        