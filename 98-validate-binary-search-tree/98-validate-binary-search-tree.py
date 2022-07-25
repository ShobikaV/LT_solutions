# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(root):
            if root is None:
                return []
            else:
                return inOrder(root.left)+[root.val]+inOrder(root.right)
        a=inOrder(root)
        if a==sorted(set(a)):
            return True
        else:
            return False