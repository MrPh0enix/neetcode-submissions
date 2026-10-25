# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out = []
        queue = deque()
        queue.append(root)

        while queue:
            res = []
            for i in range(len(queue)):
                element = queue.popleft()
                
                res.append(element.val)

                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            

            out.append(res)
        
        return out

