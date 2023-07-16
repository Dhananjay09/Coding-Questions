class Solution:

    def longestValidParentheses(self, s: str) -> int:
        max_length = 0

        l, r = 0, 0
        # traverse the string from left to right
        for ch in s:
            if ch == '(':
                l += 1
            else:
                r += 1
            if l == r:  # valid balanced parantheses substring
                max_length = max(max_length, l * 2)
            elif r > l:  # invalid case as ')' is more
                l = r = 0

        l, r = 0, 0
        s = s[::-1]
        for ch in s:
            if ch == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_length = max(max_length, l * 2)
            elif l > r:  # invalid case as '(' is more
                l = r = 0
        return max_length
