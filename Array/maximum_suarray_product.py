class Solution:
    def maxProduct(self, nums):
        m = -100000
        prod = 1
        for item in nums:
            prod *= item
            m = max(m, prod) 
            if prod == 0:
                prod = 1
        nums.reverse()
        prod = 1
        for item in nums:
            prod *= item
            m = max(m, prod)
            if prod == 0:
                prod = 1
        return m
