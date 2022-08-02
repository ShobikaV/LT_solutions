# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        def insert(temp):
            if val>temp.val:
                if temp.right:
                    insert(temp.right)
                else:
                    temp.right=TreeNode(val)
                    return 
            else:
                if temp.left:
                    insert(temp.left)
                else:
                    temp.left=TreeNode(val)
                    return 
        insert(root)
        return root
                