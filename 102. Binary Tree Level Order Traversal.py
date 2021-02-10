#102. Binary Tree Level Order Traversal
#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its level order traversal as:
#[
#  [3],
#  [9,20],
#  [15,7]
#]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leveloperation(self, queue):
        result=[]
        new_queue=[]
        for i in queue:
            result.append(i.val)
            if i.left:
                new_queue.append(i.left)
            if i.right:
                new_queue.append(i.right)
        return result, new_queue
            
    
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        queue=[root]
        out=[]
        while queue:
            result,queue= self.leveloperation(queue)
            out.append(result)
        return out
    