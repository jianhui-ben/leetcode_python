#526. Beautiful Arrangement
#Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

#perm[i] is divisible by i.
#i is divisible by perm[i].
#Given an integer n, return the number of the beautiful arrangements that you can construct.

 

#Example 1:

#Input: n = 2
#Output: 2
#Explanation: 
#The first beautiful arrangement is [1,2]:
#    - perm[1] = 1 is divisible by i = 1
#    - perm[2] = 2 is divisible by i = 2
#The second beautiful arrangement is [2,1]:
#    - perm[1] = 2 is divisible by i = 1
#    - i = 2 is divisible by perm[2] = 1


class Solution:
    def countArrangement(self, n: int) -> int:
        ##backtracking with changing options in every step
        ## here we don't need to withdraw the change we've made
        self.out=0
        def backtrack(options, cur):
            if not options:
                if cur==n:
                    self.out+=1
                return None
            for i in options:
                if i%(cur+1)==0 or (cur+1)%i==0:
                    new_options= {k for k in options if k!=i}
                    backtrack(new_options, cur+1)

        backtrack(set([i for i in range(1, n+1)]), 0)
        return self.out
        
        ## typical backtracking
        self.out=0
        def backtrack(n, cur_path):
            if len(cur_path)==n:
                self.out+=1
                return
            cur_idx=len(cur_path)+1
            for i in range(1, n+1):
                if i not in cur_path and (i%cur_idx==0 or cur_idx%i==0):
                    cur_path.append(i)
                    backtrack(n, cur_path)
                    cur_path.pop()

        backtrack(n, [])
        return self.out
        
        
        