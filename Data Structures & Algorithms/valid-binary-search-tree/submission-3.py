# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, h, l):
            if not node:
                return True

            if node.val <= l or node.val >= h:
                return False

            return (dfs(node.left, node.val, l) and dfs(node.right, h, node.val))

        return dfs(root, float('inf'), float('-inf'))
