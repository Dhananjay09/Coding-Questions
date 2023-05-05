class Solution:
    def __init__(self):
        self.arr = []

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def inorder(self, A, B):
        if not A:
            return
        self.inorder(A.left, B)
        self.arr.append(A.val)
        self.inorder(A.right, B)

    def kthsmallest(self, A, B):
        self.inorder(A, B)
        return self.arr[B - 1]
