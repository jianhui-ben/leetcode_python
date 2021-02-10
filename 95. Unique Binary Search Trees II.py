#95. Unique Binary Search Trees II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        ##recursion
        def generate(start, end):
            if start>end:
                return [None]
            all_trees=[]
            for i in range(start,end+1):
                left= generate(start, i-1)
                right=generate(i+1, end)
                
                
                for l in left:
                    for r in right:
                        cur=TreeNode(i)
                        cur.right= r
                        cur.left= l
                        all_trees.append(cur)
            return all_trees

        return generate(1, n)