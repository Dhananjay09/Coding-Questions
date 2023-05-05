class Solution:
    def maxSubArray(self, nums):
        temp = -1000000
        ans = -1000000
        for i in range(len(nums)):
            temp = max(nums[i], temp + nums[i])
            ans = max(ans, temp)
        return ans
