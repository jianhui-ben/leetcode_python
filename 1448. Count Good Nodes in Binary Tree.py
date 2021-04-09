#1448. Count Good Nodes in Binary Tree
#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

#Return the number of good nodes in the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count=0
        ## preorder dfs traverse and compare with the cur_max
        def traverse(node, cur_max):
            if not node: return
            if node.val>= cur_max:
                self.count+=1
            cur_max =max(cur_max, node.val)
            traverse(node.left, cur_max)
            traverse(node.right, cur_max)
            