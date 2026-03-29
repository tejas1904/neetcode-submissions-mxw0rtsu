# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, node: TreeNode) -> int:
        self.count = 0
        def dfs(node,maxVal):
            if node==None:
                return None
            else:
                if node.val>=maxVal:
                    self.count+=1
                                
                dfs(node.left,max(maxVal,node.val))
                dfs(node.right,max(maxVal,node.val))
        
        dfs(root,root.val)
        return self.count


