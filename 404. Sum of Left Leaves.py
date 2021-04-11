#404. Sum of Left Leaves


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ## iterative method using a stack
        ## O(n) time, O(n) space worst case; if balanced tree then O(log n)
        stored = [root]
        out=0
        while stored:
            cur_node = stored.pop(0)
            if cur_node.left and (not cur_node.left.left and not cur_node.left.right):
                out+= cur_node.left.val
            if cur_node.left:
                stored.append(cur_node.left)
            if cur_node.right:
                stored.append(cur_node.right)
        return out
    
        ## recursive with a boolean flag
        ## O(n) time O(n) space
        self.out=0
        def traverse(node, is_left):
            if not node: return
            if is_left and not node.left and not node.right:
                self.out+=node.val
            if node.left:
                traverse(node.left, True)
            if node.right:
                traverse(node.right, False)

        traverse(root, False)
        
        return self.out
    
    
                
                
            
        
        
        
        
        
        
        
        
        
        ## wrong iterative
#         self.out= 0
#         def traverse(node):
#             if not node: return 0
#             if not node.left and not node.right:
#                 return node.val
#             return traverse(node.left)

#         while root:
#             self.out+=traverse(root.left)
#             # print(self.out)
#             root = root.right
#         return self.out
        
        
