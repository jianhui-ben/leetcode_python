#138. Copy List with Random Pointer
#A linked list is given such that each node contains an additional random pointer
#which could point to any node in the list or null.

#Return a deep copy of the list.

#The Linked List is represented in the input/output as a list of n nodes. Each node 
#is represented as a pair of [val, random_index] where:

#val: an integer representing Node.val
#random_index: the index of the node (range from 0 to n-1) where random pointer points
#to, or null if it does not point to any node.

#Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited={}
        
        def dfs(old_node):
            if not old_node:
                return None
            elif old_node in visited:
                return visited[old_node]
            else: 
                new_node=Node(old_node.val, None, None)
                visited[old_node]=new_node
                new_node.next=dfs(old_node.next)
                new_node.random= dfs(old_node.random)
                return visited[old_node]
        return dfs(head)
        
