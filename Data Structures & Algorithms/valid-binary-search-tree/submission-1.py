class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (float('inf'), float('-inf'), True)  # min, max, isBST
            
            left_min, left_max, validLeft = dfs(node.left)
            right_min, right_max, validRight = dfs(node.right)
            
            if validLeft and validRight and left_max < node.val < right_min:
                min_val = min(left_min, node.val)
                max_val = max(right_max, node.val)
                return (min_val, max_val, True)
            else:
                return (0, 0, False)  # invalid subtree
        
        _, _, valid = dfs(root)
        return valid
