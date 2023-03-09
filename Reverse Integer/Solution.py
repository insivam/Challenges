class Solution(object):
    def reverse(self, x):
        nums = ""
        for num in str(x):
            nums = num + nums
        if x < 0:
            nums = "-" + nums[:-1]
        nums = int(nums)
        return 0 if nums.bit_length() >= 32 else nums