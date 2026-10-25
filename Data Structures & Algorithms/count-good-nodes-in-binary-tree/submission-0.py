# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.out = 0

        def dfs(node, maxV):
            if not node:
                return

            if node.val >= maxV:
                self.out += 1
            
            maxV = max(node.val, maxV)

            dfs(node.left, maxV)
            dfs(node.right, maxV)
        
        dfs(root, root.val)

        return self.out




            
