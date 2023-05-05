class Solution:
    def maxProfit(self, prices):
        right_max = [0 for i in range(len(prices))]
        right_max[-1] = 0
        i = len(prices)-2
        while i >= 0:
            right_max[i] = max(right_max[i+1], prices[i+1])
            i -= 1
        ans = 0
        for i in range(0, len(prices)):
            ans = max(ans, right_max[i]-prices[i])
        return ans
    