#1339. Maximum Product of Splitted Binary Tree
#Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

#Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

#Note that you need to maximize the answer before taking the mod and not after taking it.

 

#Example 1:


#Input: root = [1,2,3,4,5,6]
#Output: 110
#Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        - first get the total sum
        - for every node i, we need the sum of its subtree
        - update the res
        
        """
        self.tot_sum = 0
        def treeSum(node):
            if not node: return
            self.tot_sum += node.val
            treeSum(node.left)
            treeSum(node.right)
            
        treeSum(root)
        
        out = float('-inf')
        
        def post_order(node):
            nonlocal out
            if not node: return 0
            left_sum = right_sum = 0
            if node.left:
                left_sum = post_order(node.left)
                out = max(out, left_sum * (self.tot_sum - left_sum))
            if node.right:
                right_sum = post_order(node.right)
                out = max(out, right_sum * (self.tot_sum - right_sum))
            
            return left_sum + right_sum + node.val
            
        
        post_order(root)
        return out % (10**9 + 7)