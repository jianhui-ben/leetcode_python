#549. Binary Tree Longest Consecutive Sequence II
#Given the root of a binary tree, return the length of the longest consecutive path in the tree.

#This path can be either increasing or decreasing.

#For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
#On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

#https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

#Input: root = [1,2,3]
#Output: 2
#Explanation: The longest consecutive path is [1, 2] or [2, 1].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        
        """
        for every node, postorder(node) = len_inc, len_dec
        we return the longest length of increasing consecutive path including the node
        and  the longest length of decreasing consecutive path including the node
        
        O(N), O(H)
        """
        
        out = 0
        
        def postorder(node):
            nonlocal out
            if not node: return (0, 0)
            
            len_inc_left, len_dec_left = postorder(node.left)
            len_inc_right, len_dec_right = postorder(node.right)
            
            len_inc, len_dec = 0, 0
            if node.left:
                if node.left.val + 1 == node.val:
                    len_inc = max(len_inc, len_inc_left + 1)
                if node.left.val - 1 == node.val:
                    len_dec = max(len_dec,len_dec_left + 1)
            
            if node.right:
                if node.right.val + 1 == node.val:
                    len_inc = max(len_inc, len_inc_right + 1)
                if node.right.val - 1 == node.val:
                    len_dec = max(len_dec,len_dec_right + 1)
            
            out = max(out, len_inc + len_dec + 1)
            return (len_inc, len_dec)
                           
        
        postorder(root)
        
        return out
        
        