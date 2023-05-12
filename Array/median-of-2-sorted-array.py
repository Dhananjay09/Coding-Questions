def get_nth_element(nums1, nums2, t):
    i = 0
    j = 0
    ans = 0
    while t >= 0:
        if i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans = nums1[i]
                i += 1
            else:
                ans = nums2[j]
                j += 1
        elif i < len(nums1):
            ans = nums1[i]
            i += 1
        elif j < len(nums2):
            ans = nums2[j]
            j += 1
        t -= 1
    return ans


def findMedianSortedArrays(nums1, nums2):
    n = len(nums1) + len(nums2)
    if n % 2 != 0:
        return get_nth_element(nums1, nums2, n // 2)
    else:
        return (get_nth_element(nums1, nums2, n // 2 - 1) + get_nth_element(nums1, nums2, (n // 2))) / 2

