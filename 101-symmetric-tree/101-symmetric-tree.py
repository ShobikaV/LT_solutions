# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symm(l,r):
            if l==None and r==None:
                return True
            if l==None or r==None:
                return False
            if l.val!=r.val:
                return False
            return symm(l.left,r.right) and symm(l.right,r.left)
        return symm(root.left,root.right)
            