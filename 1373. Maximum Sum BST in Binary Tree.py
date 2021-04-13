#1373. Maximum Sum BST in Binary Tree

#Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

#Assume a BST is defined as follows:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.max_sum=float('-inf')
        
        def traverse(node):
            ## return if the node is a BST; if yes, then sum of all values
            ## also min and max need to be provided
            if not node: return (True, 0, None, None)
            is_bst_left, left_bst_sum, left_min, left_max= traverse(node.left)
            is_bst_right, right_bst_sum, right_min, right_max= traverse(node.right)
            if is_bst_left and is_bst_right:
                if not node.left and not node.right:
                    self.max_sum=max(self.max_sum, node.val)
                    return (True, node.val, node.val, node.val)
                elif not node.left and node.val<right_min:
                    self.max_sum=max(self.max_sum, node.val+right_bst_sum)
                    return (True, node.val+right_bst_sum, node.val, right_max)
                elif not node.right and node.val>left_max:
                    self.max_sum=max(self.max_sum, node.val+left_bst_sum)
                    return (True, node.val+left_bst_sum, left_min, node.val)
                elif node.left and node.right and left_max<node.val<right_min:
                    self.max_sum=max(self.max_sum, node.val+left_bst_sum+right_bst_sum)
                    return (True, node.val+left_bst_sum+right_bst_sum, left_min, right_max)
            return (False, 0, None, None)
            
        
        traverse(root) ## postorder traversal
        
        return max(0, self.max_sum)
        
        