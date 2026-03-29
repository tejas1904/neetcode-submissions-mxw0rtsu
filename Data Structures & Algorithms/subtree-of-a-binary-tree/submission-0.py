# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if (p!=None and q==None) or (p==None and q!=None):
                return False
            elif p==None and q==None:
                return True
            else:
                return (p.val==q.val) and isSame(p.left,q.left) and isSame(p.right,q.right)
        

        def DFS(root):
            if root==None:
                return False
            else:
                AtLevel = False
                if isSame(p=root,q=subRoot):
                    AtLevel = True

                return AtLevel or DFS(root.left) or DFS(root.right)
        
        return DFS(root)
        