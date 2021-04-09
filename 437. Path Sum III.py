#437. Path Sum III
#You are given a binary tree in which each node contains an integer value.

#Find the number of paths that sum to a given value.

#The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

#The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ## post order traversal and update a dictionary in every node bottom up
        
        
        self.count=0
        
        def traverse(root):
            nonlocal sum
            if not root: return defaultdict(int)
            l_path= traverse(root.left)
            r_path= traverse(root.right)
            
            temp= defaultdict(int)
            for k, v in l_path.items():
                temp[k+root.val] += v
            for k, v in r_path.items():
                temp[k+root.val] += v
            temp[root.val]+=1
            
            if sum in temp:
                self.count+=temp[sum]
            return temp
            
        traverse(root)
        
        return self.count