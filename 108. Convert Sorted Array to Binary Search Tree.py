#108. Convert Sorted Array to Binary Search Tree

#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

#For this problem, a height-balanced binary tree is defined as a binary tree in which 
#the depth of the two subtrees of every node never differ by more than 1.

#Example:

#Given the sorted array: [-10,-3,0,5,9],

#One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#      0
#     / \
#   -3   9
#   /   /
# -10  5



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## divide and concur; recursion
# time complexity: O(N); space complexity: O(log n): due to # of recursion stacks and the sapce consumed by each stack
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums)==0: return None
        if len(nums)==1: return TreeNode(val= nums[0])
        top_index= len(nums)//2
        result= TreeNode(val= nums[top_index])
        result.left= self.sortedArrayToBST(nums[:top_index])
        result.right= self.sortedArrayToBST(nums[top_index+1:])
        return result


## iterative:
