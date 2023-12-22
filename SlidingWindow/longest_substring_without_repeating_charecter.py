class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        current = 0
        dic = {}
        ans = 0
        while current < len(s):
            if s[current] in dic:
                ans = max(ans, len(dic))
                while(s[start] != s[current]):
                    dic.pop(s[start])
                    start+=1
                dic.pop(s[start])
                start+=1
            dic[s[current]] = True
            current +=1
        return max(ans, len(dic))

'''
Given a string s, find the length of the longest 
substring
 without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''