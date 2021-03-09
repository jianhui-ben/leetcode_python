509. Fibonacci Number


class Solution:
    def fib(self, n: int) -> int:
        
    ## top down recursion with mem O(n)
        if n>1:
            mem= [None]* (n+1)
            mem[0], mem[1]=0, 1
        def recur(n):
            if n==0: return 0
            if n==1: return 1
            else:
                nonlocal mem
                if mem[n]: 
                    return mem[n]
                out= recur(n-1)+recur(n-2)
                mem[n]= out
                return out
        return recur(n)
    
    ## bottom up iteration with dp
        if n==0: return 0
        if n==1 or n==2: return 1
        dp= [0]* (n+1)
        dp[1], dp[2]=1,1
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]

