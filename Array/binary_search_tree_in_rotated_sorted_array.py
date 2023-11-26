class Solution(object):

    def binary_search(self, nums, target, start, end):
        while (start <= end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def find_minimum_index(self, nums):

        if nums[0] <= nums[-1]:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)
            if nums[mid] < nums[mid - 1]:
                return mid
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    def search(self, nums, target):
        min_index = self.find_minimum_index(nums)
        if min_index == 0:
            return self.binary_search(nums, target, 0, len(nums) - 1)
        else:
            ans = self.binary_search(nums, target, min_index, len(nums) - 1)
            if ans != -1:
                return ans
            return self.binary_search(nums, target, 0, min_index - 1)


'''
33. Search in Rotated Sorted Array
Medium
24.8K
1.5K
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

'''