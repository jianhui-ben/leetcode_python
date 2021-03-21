#279. Perfect Squares

#Given an integer n, return the least number of perfect square numbers that sum to n.

#A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

#Example 1:

#Input: n = 12
#Output: 3
#Explanation: 12 = 4 + 4 + 4.

class Solution:
    def numSquares(self, n: int) -> int:
        ## BFS
        squares=[i**2 for i in range(1, int(math.sqrt(n))+1)]
        queue = [(n, 0)]
        visited=set([n])
        while queue:
            num, i = queue.pop(0)
            if num in squares:
                return i+1
            for k in squares:
                if k>num: 
                    break
                if (num-k) not in visited:
                    queue.append((num-k, i+1))
                    visited.add(num-k)

        ##recursion (a totally new idea)

        
        ## reduce search range: O(N* N**0.5)
        # dp=[float('inf')]* (n+1)
        # dp[0]=0
        # for i in range(1, n+1):
        #     squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        #     for k in squares:
        #         if i<k:
        #             break
        #         dp[i]=min(dp[i], 1+ dp[i-k])
        # return dp[-1]    
        
        
        
        
        
        # ## time O(n**2), space O(n)
        # dp=[None]* (n+1)
        # for i in range(1, n+1):
        #     if math.sqrt(i).is_integer():
        #         dp[i]=1
        #     else:
        #         out=float('inf')
        #         for k in range(1, i//2+1):
        #             out=min(out, dp[k]+ dp[i-k])
        #         dp[i]=out
        # return dp[-1]     
