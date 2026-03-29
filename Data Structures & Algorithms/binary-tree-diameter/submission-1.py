# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.global_diam = 0
        def dfs(node):
            if node==None:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            diam_at_this_node = left_depth + right_depth
            
            self.global_diam = max(self.global_diam, diam_at_this_node)

            diam_through_node = 1 + max(left_depth , right_depth)
            
            return diam_through_node
        
        dfs(root)
        return self.global_diam
        

        