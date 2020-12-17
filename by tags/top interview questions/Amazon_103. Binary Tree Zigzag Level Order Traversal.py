#103. Binary Tree Zigzag Level Order Traversal

#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its zigzag level order traversal as:
#[
#  [3],
#  [20,9],
#  [15,7]
#]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ##BFS: time O(n); space O(n)
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.out= []
        def bst(queue, level):
            if not queue: return
            if level%2==0:
                self.out.append([i.val for i in queue])
            else:
                self.out.append(reversed([i.val for i in queue]))
            temp=[]
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            bst(temp, level+1)
        bst([root], 0)
        return self.out
        
            