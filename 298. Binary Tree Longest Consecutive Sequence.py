#298. Binary Tree Longest Consecutive Sequence
#Given the root of a binary tree, return the length of the longest consecutive sequence path.

#The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

##https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

#Example 1:


#Input: root = [1,null,3,2,4,null,null,null,5]
#Output: 3
#Explanation: Longest consecutive sequence path is 3-4-5, so return 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        for every node, return longest length
        """
        out = 0
        
        def postorder(node):
            nonlocal out
            if not node: return 0
            
            longest_len = 1
            
            left_len, right_len = postorder(node.left), postorder(node.right)
            
            if node.left and node.left.val == node.val + 1:
                longest_len = max(longest_len, left_len + 1)
            if node.right and node.right.val == node.val + 1:
                longest_len = max(longest_len, right_len + 1)
            
            out = max(out, longest_len)
            # print(node.val, longest_len)
            return longest_len
            
        
        postorder(root)
        return out
        
        
        
        
        
        