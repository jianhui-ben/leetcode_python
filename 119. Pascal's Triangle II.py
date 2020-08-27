#119. Pascal's Triangle II

#Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

#Notice that the row index starts from 0.


#In Pascal's triangle, each number is the sum of the two numbers directly above it.

#Follow up:

#Could you optimize your algorithm to use only O(k) extra space?

#Example 1:

#Input: rowIndex = 3
#Output: [1,3,3,1]
#Example 2:

#Input: rowIndex = 0
#Output: [1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def dp(rowList):
            if len(rowList)==0: return [1]
            if len(rowList)==1: return [1,1]
            next= [1]*(len(rowList)+1)
            for i in range(1, len(rowList)):
                next[i]= rowList[i-1]+rowList[i]
            return next
        out=[[]]
        for c in range(rowIndex+1):
            temp=dp(out[-1])
            out.append(temp)
        return out[-1]


