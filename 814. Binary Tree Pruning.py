#814. Binary Tree Pruning
#Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

#A subtree of a node node is node plus every node that is a descendant of node.

 

#Example 1:


#Input: root = [1,null,0,0,1]
#Output: [1,null,0,null,1]
#Explanation: 
#Only the red nodes satisfy the property "every subtree not containing a 1".
#The diagram on the right represents the answer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """
        post order traversal to detemine the sum
        """
        
        def postorder(node):
            if not node: return 0
            left_res, right_res = postorder(node.left), postorder(node.right)
            if not left_res:
                node.left = None
            if not right_res:
                node.right = None
            
            return node.val + left_res + right_res
        
        if not postorder(root): return None
        
        return root