# Problem: 102. Binary Tree Level Order Traversal
# Approach: Iterative BFS
# Language: python3
# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q=deque([root])
        l=[]
        if not root:
            return []
        while q:
            ll=[]
            for _ in range(len(q)):
                node=q.popleft()
                ll.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l.append(ll[:])
        return l
