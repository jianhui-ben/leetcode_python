#1740. Find Distance in a Binary Tree

#Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

#The distance between two nodes is the number of edges on the path from one to the other.

 

#Example 1:


#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
#Output: 3
#Explanation: There are 3 edges between 5 and 0: 5-3-1-0.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        """
        O(n) time, O(H) space
        
        """
        paths = []
        found = False
        
        
        def traverse(node, target, cur_path):
            nonlocal found
            
            if not node: return
            cur_path.append(node.val)
            if node.val == target:
                paths.append(cur_path[:])
                found = True
                return
            
            traverse(node.left, target, cur_path)
            if found: return
            traverse(node.right, target, cur_path)
            cur_path.pop()
                
        
        
        
        traverse(root, p, [])
        found = False
        traverse(root, q, [])
        
        p_path, q_path = paths[0], paths[1]
        # print(p_path)
        # print(q_path)
        i = 0
        while i < (min(len(p_path), len(q_path))):
            
            if p_path[i] != q_path[i]:
                break
            i += 1
        
        return len(p_path) - i + len(q_path) - i
                