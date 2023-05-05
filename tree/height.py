class Solution:

    def height(self, root):
        if not root:
            return 0
        return 1+ max(self.height(root.left), self.height(root.right))

    def maxDepth(self, root) -> int:
        return self.height(root)
