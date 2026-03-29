class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = k
        self.ans = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.ans
