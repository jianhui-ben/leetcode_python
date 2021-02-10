#230. Kth Smallest Element in a BST

#Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

#Example 1:

#Input: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ##dfs in-order traversal: ascending order
        ##time: O(n)
        # visit=[]
        # def in_order(node):
        #     if node:
        #         in_order(node.left)
        #         visit.append(node.val)
        #         in_order(node.right)
        # in_order(root)
        # return visit[k-1]
        
        
        ## iterative method to do early stopping as long as it hits kth smallest
        ##time: O(h+k); O(h)
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            root= stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right
