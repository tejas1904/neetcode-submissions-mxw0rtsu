# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        stack  =[root]

        while stack:
            level = [ ]
            for i in range(len(stack)):
                node = stack.pop(0)
                level.append(node.val)
                
                if node.left!=None:
                    stack.append(node.left)
                if node.right!=None:
                    stack.append(node.right)

            ans.append(level)
        return ans
            

        