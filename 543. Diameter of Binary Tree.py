#543. Diameter of Binary Tree
#Given the root of a binary tree, return the length of the diameter of the tree.

#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ## dfs approach:
        self.out =0
        
        def max_depth(node):
            if not node: return 0
            l, r = max_depth(node.left), max_depth(node.right)
            self.out=max(self.out, l+r)
            return max(l, r)+1
        max_depth(root)
        return self.out
        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ## for every node, the longest path is 2+ dia(left) +dia(right)
        ## O(n), O(n)
        self.out=0
        def traverse(node):
            if not node: return -1
            l, r = traverse(node.left), traverse(node.right)
            self.out= max(self.out, 2+l+r)
            return max(l, r)+1

        traverse(root)
        return self.out