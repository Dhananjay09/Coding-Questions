class Solution:
    def merge(self, arr1, m: int, arr2, n: int):
        temp = (m + n - 1)
        left = m-1
        right = n-1
        while right >= 0:
            if left < 0 <= right:
                arr1[temp] = arr2[right]
                temp-=1
                right-=1
            elif right < 0 <= left:
                arr1[temp] = arr2[left]
                temp -= 1
                left -= 1
            elif arr1[left] < arr2[right]:
                arr1[temp] = arr2[right]
                right-=1
                temp-=1
            else:
                arr1[temp], arr1[left] = arr1[left], arr1[temp]
                temp -=1
                left-=1
        return arr1