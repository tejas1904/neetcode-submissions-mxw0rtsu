# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(r1,r2):
            if r1 and r2:
                #if root node compare values and return
                if (r1.left==None) and (r1.right==None) and (r2.left==None) and (r2.right==None):
                    return r1.val==r2.val
                #if not root comapre vals and sub branches conditions
                else:
                    return r1.val==r2.val and traverse(r1.left, r2.left) and traverse(r1.right, r2.right)
            
            else:
                if r1==None and r2==None:
                    return True
                else:
                    return False
                

            

        return traverse(p,q)
