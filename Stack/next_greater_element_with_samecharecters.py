def nextGreaterElement(n: int) -> int:
    digits = [int(item) for item in str(n)]
    l = len(digits)
    i = l-2
    while(i>=0 and digits[i]>=digits[i+1]):
        i-=1
    if i==-1:
        return -1
    j = l-1
    while(j>=0 and digits[j]<=digits[i]):
        j-=1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i+1:] = sorted(digits[i+1:])
    ans = ""
    for item in digits:
        ans+=str(item)
    ans = int(ans)
    return ans if (ans <= ((2 ** 31) - 1 )) else -1

'''
Solution - We need to find out the digit from the last which is smaller than than the next digit and then
replace that digit with the rightmost greater element

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
 
Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
'''