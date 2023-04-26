class Solution:
    # @param A : list of strings
    # @return an integer

    def evaluate(self, a, b, st):
        a = int(a)
        b = int(b)
        if st == '+':
            return a + b
        elif st == '-':
            return a - b
        elif st == '*':
            return a * b
        else:
            return a//b

    def evalRPN(self, A):
        dic = ["+", "*", "-", "/"]
        stack = [A[0], A[1]]
        ans = 0
        for i in range(2, len(A)):
            if A[i] in dic:
                second = stack.pop(-1)
                first = stack.pop(-1)
                ans = self.evaluate(first, second, A[i])
                stack.append(ans)
            else:
                stack.append(A[i])
        return ans


s = Solution()
print(s.evalRPN(["2", "2", "/"]))

