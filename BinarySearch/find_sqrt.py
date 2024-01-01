def mySqrt(x: int) -> int:
    start = 1
    end = x
    while start <= end:
        mid = (start + end)//2
        ans = mid*mid
        if (ans == x):
            return mid
        if ans<x:
            start = mid + 1
        else:
            end = mid - 1
    return end

