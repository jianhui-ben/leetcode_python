#429. N-ary Tree Level Order Traversal
#Given an n-ary tree, return the level order traversal of its nodes' values.

#Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

#Example 1:

#Input: root = [1,null,3,2,4,null,5,6]
#Output: [[1],[3,2,4],[5,6]]
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        BFS
        """
        if not root: return []
        out = []
        
        queue = [root]
        
        while queue:
            temp_queue = []
            cur_l = []
            for node in queue:
                cur_l.append(node.val)
                if node.children:
                    for child in node.children:
                        temp_queue.append(child)            
            out.append(cur_l[:])
            queue = temp_queue
        return out
                
        
        
        