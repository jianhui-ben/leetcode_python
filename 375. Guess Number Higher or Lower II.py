#375. Guess Number Higher or Lower II
#We are playing the Guessing Game. The game will work as follows:

#I pick a number between 1 and n.
#You guess a number.
#If you guess the right number, you win the game.
#If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
#Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
#Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
class Solution:
    def getMoneyAmount(self, n: int) -> int:
         ##similar to egg drop
         ##time O(N**3), space O(N**2)
         self.mem= dict()
         def dfs(start, end):
             # nonlocal mem
             if start>=end:
                 return 0
             elif end-start==1:
                 return start
             elif (start, end) in self.mem:
                 return self.mem[(start, end)]
             out= float('inf')
             for i in range(start, end+1):
                 guess_lower= dfs(start, i-1)
                 guess_higher= dfs(i+1, end)
                 out= min(out, max(guess_lower+i, guess_higher+i))
             self.mem[(start, end)]=out
             return self.mem[(start, end)]
         return dfs(1, n)
        
        
         to improve it, we can use binary search to optimize the search in each subproblem:
         O(N**2 * log N)
        self.mem= dict()
        def dfs(start, end):
            # nonlocal mem
            if start>=end:
                return 0
            elif end-start==1:
                return start
            elif (start, end) in self.mem:
                return self.mem[(start, end)]
            out= float('inf')
            mid=(start+end)//2
            for i in range(mid, end+1):
                guess_lower= dfs(start, i-1)
                guess_higher= dfs(i+1, end)
                out= min(out, max(guess_lower+i, guess_higher+i))
            self.mem[(start, end)]=out
            return self.mem[(start, end)]
        return dfs(1, n)        
        
        