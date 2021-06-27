#364. Nested List Weight Sum II
#You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

#The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

#The weight of an integer is maxDepth - (the depth of the integer) + 1.

#Return the sum of each integer in nestedList multiplied by its weight.

 

#Example 1:


#Input: nestedList = [[1,1],2,[1,1]]
#Output: 8

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#         """
#         O(n), O(d); use O(n) to get depth and then calculate the result
#         """
#         self.max_depth = float('-inf')
        
#         def get_depth(nestedInt, depth):
#             if nestedInt == []:
#                 return
#             if nestedInt.isInteger():
#                 self.max_depth = max(self.max_depth, depth)
#             for next_nestedInt in nestedInt.getList():
#                 get_depth(next_nestedInt, depth + 1)

#         for nestedInt in nestedList:
#             get_depth(nestedInt, 1)
        
#         def traverse(nestedInt, depth):
#             if nestedInt == []:
#                 return
#             if nestedInt.isInteger():
#                 self.out += (self.max_depth - depth + 1) * nestedInt.getInteger()
#             for next_nestedInt in nestedInt.getList():
#                 traverse(next_nestedInt, depth + 1)
        
#         self.out = 0
#         for nestedInt in nestedList:
#             traverse(nestedInt, 1)
        
#         return self.out
        
        
        """
        get depth of every single NestedInteger, 
        store its value and depth in []
        O(n), O(d)
        """ 
        stored = defaultdict(int) ## key: depth; value: sum on this depth so far
        
        self.max_depth = 0
        
        def traverse(nestedInt, cur_depth):
            nonlocal stored
            if nestedInt == []:
                return
            
            if nestedInt.isInteger():
                stored[cur_depth] += nestedInt.getInteger()
                self.max_depth = max(self.max_depth, cur_depth)
                return
            for nextNestedInt in nestedInt.getList():
                traverse(nextNestedInt, cur_depth + 1)
            
        for nestedInt in nestedList:
            traverse(nestedInt, 1)
        
        output = 0
        for depth, val in stored.items():
            output += (self.max_depth - depth + 1) * val
            
        return output
        
        
        
        
        
        
        
        
        
        