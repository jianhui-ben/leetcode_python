#887. Super Egg Drop

#You are given k eggs, and you have access to a building with n floors labeled from 1 to n.

#Each egg is identical in function, and if an egg breaks, you cannot drop it again.

#You know that there exists a floor f with 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

#Each move, you may take an egg (if you have an unbroken one) and drop it from any floor x (with 1 <= x <= n).

#Your goal is to know with certainty what the value of f is.

#Return the minimum number of moves that you need to know with certainty the value of f.

 

#Example 1:

#Input: k = 1, n = 2
#Output: 2
#Explanation: 
#Drop the egg from floor 1. If it breaks, we know with certainty that f = 0.
#Otherwise, drop the egg from floor 2. If it breaks, we know with certainty that f = 1.
#If it did not break, then we know with certainty f = 2.
#Hence, we needed 2 moves in the worst case to know what f is with certainty.


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        ## dp with mem: # of subproblems * time complexity of the subproblme ignoring the recursion part
        ## time O(K* N * N)
        mem= dict()
        def dp(k, n):
            if k==1: return n
            if n==0: return 0
            if (k, n) in mem: return mem[(k, n)]
            out= float('inf')
            ##we can choose to throw the egg on the i th floor
            for i in range(1, n+1):
                out= min(out, max(dp(k-1, i-1), dp(k,n-i))+1)
            mem[(k, n)]=out
            return mem[(k, n)]
        return dp(k, n)
    
    
        ## to optimize this code, we can use binary search to look for the i to try
        ## # of subproblems are still (K * N), but to solve each subproblem, it takes log n
        ## total O(K * N * logn)
        mem= dict()
        def dp(k, n):
            if k==1: return n
            if n==0: return 0
            if (k, n) in mem: return mem[(k, n)]
            out= float('inf')
            lo, hi =1, n
            while lo <=hi:
                mid =(lo+hi)//2
                broken, not_broken = dp(k-1, mid-1), dp(k, n-mid)
                if broken> not_broken:
                    out= min(out, broken+1)
                    hi=mid-1
                else:
                    out = min(out, not_broken+1)
                    lo = mid+1
            mem[(k, n)] = out
            return mem[(k, n)]
        return dp(k, n)
                
            
    
        
        
    
    
    