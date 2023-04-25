def solve(A):
    stack = []
    for i in range(0, len(A)):
        if len(stack) == 0:
            stack.append(A[i])
            continue
        f = False
        while len(stack) >= 1 and stack[-1] == A[i]:
            f = True
            stack.pop(-1)
        if not f:
            stack.append(A[i])
    ans = ""
    for item in stack:
        ans += item
    return ans
