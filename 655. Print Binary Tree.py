#655. Print Binary Tree
#Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

#The height of the tree is height and the number of rows m should be equal to height + 1.
#The number of columns n should be equal to 2height+1 - 1.
#Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
#For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
#Continue this process until all the nodes in the tree have been placed.
#Any empty cells should contain the empty string "".
#Return the constructed matrix res.

 

#Example 1:


#Input: root = [1,2]
#Output: 
#[["","1",""],
# ["2","",""]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_height(node):
            if not node: return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        height = get_height(root)

        out = [['' for _ in range(2 ** height - 1)] for _ in range(height)]
        
        col = 2 ** height - 2
        
        def bfs(start_col, end_col, node, row):
            nonlocal out
            if not node or row == len(out): return
            
            middle = (start_col + end_col) // 2
            out[row][middle] = str(node.val)
            bfs(start_col, middle - 1, node.left, row + 1)
            bfs(middle + 1, end_col, node.right, row + 1)

        
        bfs(0, col, root, 0)
        
        return out
        