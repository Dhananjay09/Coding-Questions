class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        while A % 3 != 0:
            ans += 1
            A += 1
        while B % 3 != 0:
            ans += 1
            B -= 1
        ans += ((B - A) * 2) // 3
        return ans

