class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        first_str_dic = {}
        second_str_dic = {}

        for i in range(len(s)):
            if s[i] not in first_str_dic:
                first_str_dic[s[i]] = t[i]
            if t[i] not in second_str_dic:
                second_str_dic[t[i]] = s[i]
            if first_str_dic[s[i]] != t[i] or second_str_dic[t[i]] != s[i]:
                return False
        return True


str1 = "Dhananjay Singh"
str2 = "Dhananjay Singz"
print(Solution().isIsomorphic(str1, str2))
