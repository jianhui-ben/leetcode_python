#257. Binary Tree Paths

#Given a binary tree, return all root-to-leaf paths.

#Note: A leaf is a node with no children.

#Example:

#Input:

#   1
# /   \
#2     3
# \
#  5

#Output: ["1->2->5", "1->3"]

#Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # ##recursion
        # out=[]
        # def recursion(node, cur_path):
        #     if node:
        #         cur_path+= str(node.val)
        #         if not node.left and not node.right:
        #             out.append(cur_path)
        #         else:
        #             cur_path+='->'
        #             recursion(node.left, cur_path)
        #             recursion(node.right, cur_path)
        # recursion(root, '')
        # return out
    
        ## iteration:
        if not root: return []
        stack=[(root, str(root.val))]
        out=[]
        while stack:
            cur_node, path=stack.pop()
            if not cur_node.left and not cur_node.right:
                out.append(path)
            if cur_node.left:
                stack.append((cur_node.left, path+'->'+ str(cur_node.left.val)))
            if cur_node.right:
                stack.append((cur_node.right, path+'->'+ str(cur_node.right.val)))
        return out
            
