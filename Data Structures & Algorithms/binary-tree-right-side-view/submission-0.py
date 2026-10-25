# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        out = []

        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                elem = q.popleft()
                level.append(elem.val)

                if elem.right:
                    q.append(elem.right)
                if elem.left:
                    q.append(elem.left)
                
            out.append(level[0])
        
        return out

