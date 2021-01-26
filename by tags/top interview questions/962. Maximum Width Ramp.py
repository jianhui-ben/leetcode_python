#962. Maximum Width Ramp

#Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

#Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

 

#Example 1:

#Input: [6,0,8,2,1,5]
#Output: 4
#Explanation: 
#The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ## O(n)
        candidates, out=[], 0
        for i, v in enumerate(A):
            if not candidates or v<A[candidates[-1]]:
                candidates.append(i)
        
        for j in range(len(A)-1, -1, -1):
            while candidates and A[j]>=A[candidates[-1]]:
                out= max(out, j- candidates[-1])
                candidates.pop()
            if not candidates or j<=candidates[-1]:
                break
        return out
                
        
        ## binary search O(n log n)
#         candidates=[]
#         out=0
#         for i, v in enumerate(A):
#             if not candidates or A[candidates[-1]]>v:
#                 candidates.append(i)
#             else:
#                 ##binary search
#                 low, high= 0, len(candidates)
#                 while low< high:
#                     mid=(low+high)//2
#                     if A[candidates[mid]]<=v:
#                         high=mid
#                     else:
#                         low=mid+1
#                 out= max(out, i-candidates[low])
#         return out
            