# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def maxDepthh(root):
            if root==None:
                return 0
            else:
                maxdepth = max(maxDepthh(root.left),maxDepthh(root.right))
                return 1+maxdepth
        
        return maxDepthh(root)
        