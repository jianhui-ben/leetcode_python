#107. Binary Tree Level Order Traversal II

#Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
#(ie, from left to right, level by level from leaf to root).

#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its bottom-up level order traversal as:
#[
#  [15,7],
#  [9,20],
#  [3]
#]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## iterative method 
#time complexity: O(# of vertices + # of edges); space complexity: O(# of vertices) O (n)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        traversal= [[root]]
        result= deque()
        while traversal:
            level= traversal.pop()
            cur_level, next_level=[], []
            for i in level:
                if i is not None: 
                    cur_level.append(i.val)
                    next_level+=[i.left, i.right]
            result.appendleft(cur_level)
            if not all(v is None for v in next_level):
                traversal.append(next_level)
        return list(result)
