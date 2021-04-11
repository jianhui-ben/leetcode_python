#1120. Maximum Average Subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        ## post-order traversal
        ## O(n) time,  O(n) space
        self.out= []
        
        ## return the sum of the tree and # of nodes in this tree
        def traverse(node):
            if not node: return 0, 0
            sum_left, cnt_left = traverse(node.left)
            sum_right, cnt_right =traverse(node.right)
            new_sum, new_cnt = sum_left+sum_right+node.val, cnt_left+cnt_right+1
            self.out.append((new_sum, new_cnt))
            return new_sum, new_cnt
            
        traverse(root)
        
        return max([float(s)/c for s, c in self.out])
        