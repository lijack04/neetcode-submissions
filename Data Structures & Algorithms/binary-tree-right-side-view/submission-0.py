# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque()
        queue.append(root) if root else None

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()
                if i == length - 1:
                    res.append(node.val)
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
            
        


        return res