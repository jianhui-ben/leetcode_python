#1007. Minimum Domino Rotations For Equal Row

#In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
#(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

#We may rotate the ith domino, so that A[i] and B[i] swap values.

#Return the minimum number of rotations so that all the values in A 
#are the same, or all the values in B are the same.

#If it cannot be done, return -1.

 

#Example 1:


#Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
#Output: 2
#Explanation: 
#The first figure represents the dominoes as given by A and B: before we do any rotations.
#If we rotate the second and fourth dominoes, we can make every value in the 
#top row equal to 2, as indicated by the second figure.


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ##brute force
        ##figure out which values will be used for the row:
        ## then figure out rotations to make A or B will have the fewer rounds
        candidates=set([A[0],B[0]])
        for i in range(1, len(A)):
            if len(candidates)== 0:
                return -1
            temp = candidates.copy()
            for c in temp:
                if c not in [A[i], B[i]]:
                    candidates.remove(c)
        out=[]
        for c in candidates:
            countA, countB=0, 0
            for i in range(len(A)):
                if A[i]!=c:
                    countA+=1
                if B[i]!=c:
                    countB+=1
            out+=[countA, countB]
        
        return min(out)
                    