class Solution:

    def is_palindrome(self, s):
        if len(s) == 0:
            return True
        return s == s[::-1]

    def longestPalindrome(self, s):
        for i in range(len(s)):
            pass
