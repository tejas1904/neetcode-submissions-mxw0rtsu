# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        node = root
        stack = []
        prev  = None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop(-1)
            if prev is not None:
                if prev < node.val:
                    prev = node.val
                else:
                    return False
            else:
                prev = node.val
            
            node = node.right
        return True
            

            
