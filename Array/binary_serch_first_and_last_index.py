class Solution:

    def bst(self, nums, target, is_first):
        left = 0
        right = len(nums) - 1
        ind = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ind = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ind

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        left = self.bst(nums, target, True)
        right = self.bst(nums, target, False)
        return [left, right]
