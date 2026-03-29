# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def height(node):
            if not node:
                return 0
            elif root.left or root.right:
                left_h = height(node.left)
                right_h = height(node.right)

                thisDiam  = left_h + right_h
                self.maxDiameter = max(self.maxDiameter, thisDiam)                
                return 1 + max(left_h, right_h)
            else:
                return 1

        height(root)
        return self.maxDiameter
