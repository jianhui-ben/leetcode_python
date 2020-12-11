#938. Range Sum of BST

#Given the root node of a binary search tree, return the sum of values of all 
#nodes with a value in the range [low, high].

 

#Example 1:


#Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#Output: 32


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ##recursion
#     def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#         self.out=0
#         def recursion(root, low, high):
#             if not root: return
#             if root.val<low:
#                 recursion(root.right, low, high)
#             elif root.val>high:
#                 recursion(root.left, low, high)
#             elif root.val<= high and root.val>=low:
#                 self.out+=root.val
#                 recursion(root.left, low, high)
#                 recursion(root.right, low, high)
                
#         recursion(root, low, high)
#         return self.out
    
    ##iterative method
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        out= 0
        queue= [root]
        while queue:
            cur_node= queue.pop()
            if not cur_node: continue
            if low<=cur_node.val<= high:
                out+=cur_node.val
            if low< cur_node.val:
                queue.append(cur_node.left)
            if high>cur_node.val:
                queue.append(cur_node.right)
        return out