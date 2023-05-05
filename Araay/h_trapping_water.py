class Solution:
    def trap(self, arr):
        res = 0
        n = len(arr)
        left_arr = []
        for i in range(0, n):
            if i == 0:
                left_arr.append(arr[i])
                continue
            left_arr.append(max(left_arr[-1], arr[i]))
        right_arr = [0 for i in range(n)]
        for i in reversed(range(n)):
            if i == n - 1:
                right_arr[i] = arr[i]
                continue
            right_arr[i] = max(right_arr[i + 1], arr[i])
        for i in range(0, n):
            res = res + min(left_arr[i], right_arr[i]) - arr[i]
        return res
