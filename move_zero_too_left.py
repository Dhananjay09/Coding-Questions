class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        i = 0
        while(i<len(nums)):
            if nums[i]==0:
                nums[i],nums[left]=nums[left], nums[i]
                left+=1
            i+=1
        
