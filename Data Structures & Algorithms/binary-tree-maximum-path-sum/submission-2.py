# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_seen = -float('inf')
        def dfs(node):
            if node==None:
                return 0
            
            else:
                
                left_subtree_wt = dfs(node.left)
                right_subtree_wt = dfs(node.right)

                node_wt = node.val

                node_plus_left = node_wt + left_subtree_wt
                node_plus_right = node_wt +  right_subtree_wt
                node_plus_right_plus_left = node_wt + left_subtree_wt + right_subtree_wt

                best_path_sum = max(node_wt,
                node_plus_left,
                node_plus_right,
                node_plus_right_plus_left)
                
                self.max_seen =  max(self.max_seen, best_path_sum)
                
                return max(node_wt,node_plus_left,node_plus_right,)
        
        dfs(root)
        return self.max_seen
        