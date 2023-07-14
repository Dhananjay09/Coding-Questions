class Solution:
    def topKFrequent(self, nums, k):
        dic = {}

        for item in nums:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        values = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(0, k):
            ans.append(values[i][0])
        return ans

# 347. Top K Frequent Elements

