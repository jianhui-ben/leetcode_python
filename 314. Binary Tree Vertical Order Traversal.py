#Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

#If two nodes are in the same row and column, the order should be from left to right.

 

#Example 1:


#Input: root = [3,9,20,null,null,15,7]
#Output: [[9],[3,15],[20],[7]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ## approach 2: BST
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        out=collections.defaultdict(list)
        queue= [(root, 0)]
        while queue:
            node, i= queue.pop(0)
            out[i].append(node.val)
            if node.left:
                queue.append((node.left, i-1))
            if node.right:
                queue.append((node.right, i+1))
        return [val for _, val in sorted(out.items())]
        
        
        

    
#     ## approach 1: dfs to save both hidth and width
#     def verticalOrder(self, root: TreeNode) -> List[List[int]]:
#         out=collections.defaultdict(list)
#         def dfs(node, i, h):
#             if node:
#                 out[i].append((node.val, h))
#                 dfs(node.left,i-1, h+1)
#                 dfs(node.right, i+1, h+1)
#         dfs(root, 0, 0)
        
#         return [[val for val, h in sorted(value, key= lambda x: x[1])] for _, value in sorted(out.items())]
        