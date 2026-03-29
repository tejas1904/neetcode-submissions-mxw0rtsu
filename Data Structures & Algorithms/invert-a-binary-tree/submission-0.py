# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = root

        def invert(root):
            if root==None:
                return None
            elif root.left or root.right:
                tmpLeft = invert(root.left)
                tmpRight = invert(root.right)

                root.right = tmpLeft
                root.left = tmpRight
                
                return root
            else:
                return root
        
        return invert(root)