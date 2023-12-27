class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        all_permutaions = []
        for i in range(0, len(nums)):
            cl = [nums[i]]
            rl = nums[:i] + nums[i+1:]
            prmts = self.permute(rl)
            for ans in prmts:
                all_permutaions.append(cl + ans)
        return all_permutaions

'''

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

'''