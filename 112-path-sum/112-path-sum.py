# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathsum(root,tsum):
            if root==None:
                return False
            tsum-=root.val
            if root.left==None and root.right==None:
                if tsum==0:
                    return True
            else:
                return pathsum(root.left,tsum) or pathsum(root.right,tsum)
        return pathsum(root,targetSum)