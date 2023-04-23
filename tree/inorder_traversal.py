class Solution:
    def __init__(self):
        self.ans = []

    def trv(self, root):
        if not root:
            return
        self.trv(root.left)
        self.ans.append(root.val)
        self.trv(root.right)

    def inorderTraversal(self, root):
        self.trv(root)
        return self.ans
