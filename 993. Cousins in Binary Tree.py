#993. Cousins in Binary Tree
#In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

#Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

#We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

#Return true if and only if the nodes corresponding to the values x and y are cousins.

 

#Example 1:


#Input: root = [1,2,3,4], x = 4, y = 3
#Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        level order traversal
        O(n), O(log n)
        """
        level_arr =  [root]
        
        while level_arr:
            next_level_arr, next_level_set = [], set()
            for node in level_arr:
                if node.val == x or node.val == y:
                    return False
                if node.left and node.right:
                    if set([node.left.val, node.right.val]) == set([x, y]):
                        return False
                    
                if node.left:
                    next_level_arr.append(node.left)
                    next_level_set.add(node.left.val)
                
                if node.right:
                    next_level_arr.append(node.right)
                    next_level_set.add(node.right.val)
            
            if x in next_level_set and y in next_level_set:
                return True
            elif x in next_level_set or y in next_level_set:
                return False
            level_arr = next_level_arr
            
                    
            
        
        
        
        