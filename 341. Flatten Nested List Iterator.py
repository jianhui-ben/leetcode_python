#341. Flatten Nested List Iterator

#Given a nested list of integers, implement an iterator to flatten it.

#Each element is either an integer, or a list -- whose elements may also be integers or other lists.

#Example 1:

#Input: [[1,1],2,[1,1]]
#Output: [1,1,2,1,1]
#Explanation: By calling next repeatedly until hasNext returns false, 
#             the order of elements returned by next should be: [1,1,2,1,1].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.l=[]
        def getall(nestedList):
            # while nestedList.getInteger() or nestedList.getList():
            for ele in nestedList:
                if ele.isInteger():
                    self.l.append(ele.getInteger())
                else:
                    getall(ele.getList())
        getall(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.l.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.l)!=0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
