#992. Subarrays with K Different Integers

#Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

#(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

#Return the number of good subarrays of A.

 

#Example 1:

#Input: A = [1,2,1,2,3], K = 2
#Output: 7
#Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#Example 2:

#Input: A = [1,2,1,3,4], K = 3
#Output: 3
#Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ## brute force N**2
        #but we can optimize it to O(n) using a two pointer and a hashtable
        ## another thing is that it requires exactly K
        ## which is equivalent to atMOst(K)- atMost(k-1)
        print(self.atMost(A, K))
        print(self.atMost(A, K-1))
        return self.atMost(A, K)- self.atMost(A, K-1)
    
    def atMost(self, A, K):
        if K==0: return 0
        import collections
        stored= collections.defaultdict()
        start, out=0, 0
        
        for end in range(len(A)):
            if A[end] not in stored: stored[A[end]]=1
            else: stored[A[end]]+=1
            
            while len(stored)>K:
                if stored[A[start]]==1:
                    stored.pop(A[start])
                else: stored[A[start]]-=1
                start+=1
            out+=end-start+1
        return out