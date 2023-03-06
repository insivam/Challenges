def buildArray(self, nums):
    ans = []
    for c, i in enumerate(nums):
        ans.append(nums[nums[c]])
    return ans