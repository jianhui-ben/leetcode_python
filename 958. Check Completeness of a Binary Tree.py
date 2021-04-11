#958. Check Completeness of a Binary Tree
#Given the root of a binary tree, determine if it is a complete binary tree.

#In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        ## BFS
        ## O(n), space O(n)
        from collections import deque
        stored = deque([root])
        while stored:
            node = stored.popleft()
            if not node:
                break
            if node.left:
                stored.append(node.left)
            else:
                stored.append(None)
            if node.right:
                stored.append(node.right)
            else:
                stored.append(None)
        for i in stored:
            if i is not None:
                return False
 
        return True
        
        
        
        