class Solution:
    def invertTree(self, root):
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right=root.right, root.left
        return root
