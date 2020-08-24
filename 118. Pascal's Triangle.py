#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


#In Pascal's triangle, each number is the sum of the two numbers directly above it.

#Example:

#Input: 5
#Output:
#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]

def dp(rowList):
    if len(rowList)==0: return [1]
    if len(rowList)==1: return [1,1]
    next= [1]*(len(rowList)+1)
    for i in range(1, len(rowList)):
        next[i]= rowList[i-1]+rowList[i]
    return next



dp(dp([1,2,1]))



##dynamic programming
## time O(n**2); space O(n**2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def dp(rowList):
            if len(rowList)==0: return [1]
            if len(rowList)==1: return [1,1]
            next= [1]*(len(rowList)+1)
            for i in range(1, len(rowList)):
                next[i]= rowList[i-1]+rowList[i]
            return next
        out=[[]]
        for c in range(numRows):
            temp=dp(out[-1])
            out.append(temp)
        return out[1:]
            