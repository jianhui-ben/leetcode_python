#199. Binary Tree Right Side View
#Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#Example:

#Input: [1,2,3,null,5,null,4]
#Output: [1, 3, 4]
#Explanation:

#   1            <---
# /   \
#2     3         <---
# \     \
#  5     4       <---


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ##level order traversal
        if not root: return []
        queue=[root]
        out=[]
        while queue:
            out.append(queue[-1].val)
            temp=[]
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue= temp
        return out
            
            
        