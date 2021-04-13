#1214. Two Sum BSTs

#Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        ## not sure the time complexity
        if root1 and root2:
            if root1.val + root2.val ==target:
                return True
            elif root1.val + root2.val >target:
                return self.twoSumBSTs(root1, root2.left, target) or self.twoSumBSTs(root1.left, root2, target)
            else:
                return self.twoSumBSTs(root1, root2.right, target) or self.twoSumBSTs(root1.right, root2, target)
        return False
            
        
        
        
        ## brute force into two sum
        ## O(n)
        arr_1, arr_2 = [], []
        
        def traverse(node, arr):
            if not node: return
            traverse(node.left, arr)
            arr.append(node.val)
            traverse(node.right, arr)
        
        traverse(root1, arr_1)
        traverse(root2, arr_2)
        
        ## solve a two sum using hashtable
        hash_1=set()
        for i in arr_1:
            hash_1.add(target-i)
        
        for i in arr_2:
            if i in hash_1:
                return True
        return False
        
        
        
        
        ## use two pointer to combine two sorted arr:
        # combine=[]
        # while arr_1 and arr_2:
        #     if arr_1[0]<=arr_2[0]:
        #         combine.append(arr_1.pop(0))
        #     else:
        #         combine.append(arr_2.pop(0))
        # if arr_1:
        #     combine+=arr_1
        # else:
        #     combine+=arr_2
            
        # ## two sum in an sorted input arr:
        # left, right = 0, len(combine)-1
        # while left<right:
        #     if combine[left]+combine[right]==target:
        #         return True
        #     elif combine[left]+combine[right]>target:
        #         right-=1
        #     else:
        #         left+=1
        # return False
            