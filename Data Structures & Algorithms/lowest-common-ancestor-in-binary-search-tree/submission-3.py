# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ansNode = None
        
        def dfs(root):
            if root==None:
                return False
            else:
                presentInLeft = dfs(root.left)
                presentInRight = dfs(root.right)
                presentInSelf = (root.val == p.val) or (root.val == q.val)

                if presentInLeft + presentInRight + presentInSelf>=2:
                    self.ansNode = root
                    return True
                else:
                    return presentInSelf or presentInLeft or presentInRight
        
        dfs(root)

        return self.ansNode
 
                