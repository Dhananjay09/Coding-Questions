class Solution:
    def move_zero_to_left(self, nums) -> None:
        left = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1
        return nums


cls = Solution()
test_array = [0, 1, 0, 3, 12]
print(f"INPUT - {test_array}")
print(f"OUTPUT - {cls.move_zero_to_left(test_array)}")
