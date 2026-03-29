# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root==None:
                return (0,True)
            else:
                left_h, lbal = height(root.left)
                right_h, rbal = height(root.right)
                
                cond2 = lbal and rbal
                cond1 = abs(left_h-right_h)<=1
                
                return ( 1+max(left_h , right_h), cond1 and cond2)
        
        _,ret = height(root)
        return ret

        