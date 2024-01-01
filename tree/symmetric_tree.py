class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def check(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.check(left.left, right.right) and self.check(left.right, right.left)
        return False

    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

'''
101. Symmetric Tree
Easy
14.7K
356
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false

'''