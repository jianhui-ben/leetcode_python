#863. All Nodes Distance K in Binary Tree
#We are given a binary tree (with root node root), a target node, and an integer value K.

#Return a list of the values of all nodes that have a distance K from the target node.  
#The answer can be returned in any order.

 

#Example 1:

#Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

#Output: [7,4,1]

#Explanation: 
#The nodes that are a distance 2 from the target node (with value 5)
#have values 7, 4, and 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ##time O(N), space O(N)
        def dfs(node, parent):
            if node:
                node.parent= parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        
        queue=[(target,0)]
        out=[]
        seen=set([target])
        while queue:
            cur_node, cur_distance= queue.pop(0)
            if cur_distance== K:
                out.append(cur_node.val)
            elif cur_distance<= K:
                for next_node in (cur_node.left, cur_node.right, cur_node.parent):
                    if next_node and next_node not in seen:
                        queue.append((next_node, cur_distance+1))
                        seen.add(next_node)
        return out