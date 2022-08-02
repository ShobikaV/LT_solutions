# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d=[]
        def search(root):
            if root==None:
                return False
            if k-root.val in d:
                return True
            else:
                d.append(root.val)
            return search(root.left) or search(root.right)
        return search(root)
        