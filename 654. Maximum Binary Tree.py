#654. Maximum Binary Tree

#You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

#Create a root node whose value is the maximum value in nums.
#Recursively build the left subtree on the subarray prefix to the left of the maximum value.
#Recursively build the right subtree on the subarray suffix to the right of the maximum value.
#Return the maximum binary tree built from nums.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        ## tree traversal with recursion
        ## time O(n**2), space O(n)
        
        if not nums:
            return None
        
        
        max_val, max_i= float('-inf'), None
        for i, v in enumerate(nums):
            if v>max_val:
                max_val = v
                max_i = i
        
        root =TreeNode(val=max_val)
        root.left= self.constructMaximumBinaryTree(nums[:max_i])
        root.right= self.constructMaximumBinaryTree(nums[max_i+1:])
        
        
        return root
        