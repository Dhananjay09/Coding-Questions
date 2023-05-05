def check_reach(arr):
    max_reach = arr[0]
    for i in range(1, len(arr)):
        if max_reach < i:
            return False
        max_reach = max(max_reach, arr[i]+i)
    return True


def majorityElement(nums):
    dic = {}
    ans = int((len(nums)+1)/2)
    for item in nums:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
        if dic[item] >= ans:
            return item
