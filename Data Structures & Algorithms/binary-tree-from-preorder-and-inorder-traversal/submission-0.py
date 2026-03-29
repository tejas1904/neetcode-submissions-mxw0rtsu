# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def builder(preorder,inorder):
            if len(inorder)==len(preorder)==0:
                return None
            if len(inorder)==len(preorder)==1:
                node = TreeNode(val = preorder[0])
                return node
            else:
                node = TreeNode(val = preorder[0])
                i = inorder.index(preorder[0])
            
                node.left = builder(preorder[1:i+1],inorder[:i])
                node.right = builder(preorder[i+1:] , inorder[i+1:])

            return node
        
        return builder(preorder,inorder)