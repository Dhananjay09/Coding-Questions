class Solution:
    def climbStairs(self, n):
        res = [1, 2, 3]
        if n <= 3:
            return res[n-1]
        for i in range(3, n):
            res.append(res[i-1]+res[i-2])
        return res[n-1]
