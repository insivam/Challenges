def threeSum(nums):
    answer = []
    nums.sort()
    for c, i in enumerate(nums):
        for d, j in enumerate(nums[c+1:]):
            for k in nums[c+d+2:]:
                if i + j + k == 0 and [i, j, k] not in answer:
                    answer.append([i, j, k])     
    return answer
