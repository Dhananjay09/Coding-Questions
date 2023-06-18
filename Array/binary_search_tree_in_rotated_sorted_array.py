class Solution:

    def bs(self, arr, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums, target) -> int:
        temp = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                temp = i + 1
                break

        if temp != 0:

            ans1 = self.bs(nums, target, 0, temp - 1)

            if ans1 != -1:

                return ans1

            else:

                return self.bs(nums, target, temp, len(nums) - 1)

        return self.bs(nums, target, 0, len(nums) - 1)

