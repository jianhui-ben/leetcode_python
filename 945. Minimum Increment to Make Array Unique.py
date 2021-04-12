#945. Minimum Increment to Make Array Unique

#Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

#Return the least number of moves to make every value in A unique.

 

#Example 1:

#Input: [1,2,2]
#Output: 1
#Explanation:  After 1 move, the array could be [1, 2, 3].

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        count=0
        
        stored= []
        
        for i in A:
            if stored and stored[-1]>=i:
                count+=stored[-1]+1-i
                stored.append(stored[-1]+1)
            else:
                stored.append(i)
                
        return count