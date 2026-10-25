# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = deque()
        queue.append(root)

        while queue:
            res = []
            for i in range(len(queue)):
                element = queue.popleft()
                if element:
                    res.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
            if res:
                out.append(res)
        
        return out

