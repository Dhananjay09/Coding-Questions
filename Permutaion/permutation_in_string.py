class Solution:

    def check_sbst(self, dic, s):
        new_dic = dic.copy()
        for ch in s:
            if ch in new_dic:
                if new_dic[ch] >1:
                    new_dic[ch] -=1
                else:
                    new_dic.pop(ch)
                continue
            else:
                return False
        return True


    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for ch in s1:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        i = 0
        while (i<len(s2)):
            if s2[i] in dic:
                if i+len(s1) <= len(s2) and self.check_sbst(dic, s2[i:i+len(s1)]):
                    return True
            i+=1
        return False

'''

567. Permutation in String
Medium
10.9K
366
Companies
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''