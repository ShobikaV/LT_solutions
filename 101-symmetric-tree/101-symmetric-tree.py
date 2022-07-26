# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symm(temp1,temp2):
            if temp1==None and temp2==None:
                return True
            if temp1==None or temp2==None:
                return False
            if temp1.val!=temp2.val:
                return False
            return symm(temp1.left,temp2.right) and symm(temp1.right,temp2.left)
        return symm(root.left,root.right)
            