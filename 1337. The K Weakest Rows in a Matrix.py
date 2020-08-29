#given a m * n matrix mat of ones (representing soldiers) and zeros 
#(representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

#a row i is weaker than row j, if the number of soldiers in row i is 
#less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

#example 1:

#input: mat = 
#[[1,1,0,0,0],
# [1,1,1,1,0],
# [1,0,0,0,0],
# [1,1,0,0,0],
# [1,1,1,1,1]], 
#k = 3
#output: [2,0,3]
#explanation: 
#the number of soldiers for each row is: 
#row 0 -> 2 
#row 1 -> 4 
#row 2 -> 1 
#row 3 -> 2 
#row 4 -> 5 
#rows ordered from the weakest to the strongest are [2,0,3,1,4]
#example 2:

#input: mat = 
#[[1,0,0,0],
# [1,1,1,1],
# [1,0,0,0],
# [1,0,0,0]], 
#k = 2
#output: [0,2]
#explanation: 
#the number of soldiers for each row is: 
#row 0 -> 1 
#row 1 -> 4 
#row 2 -> 1 
#row 3 -> 1 
#rows ordered from the weakest to the strongest are [0,2,3,1]
 

#constraints:

#m == mat.length
#n == mat[i].length
#2 <= n, m <= 100
#1 <= k <= m
#matrix[i][j] is either 0 or 1.
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        import numpy
        rank=[]
        for i in range(len(mat)):
            try:
                rank.append(mat[i].index(0))
            except:
                rank.append(len(mat[i]))
                            
        #sort_rank=numpy.argsort(rank)  ##something wrong with the numpt.argsort
        sort_rank=sorted(range(len(rank)),key=rank.__getitem__)
        return sort_rank[0:k]