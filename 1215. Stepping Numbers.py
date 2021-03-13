#1215. Stepping Numbers
#A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.

#Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.

 

#Example 1:

#Input: low = 0, high = 21
#Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        #dfs: time O(log 10 N), space O(log 10 N)
        out =set()
        def dfs(num):
            nonlocal out
            if num<0 or num >high:
                return 
            if low <= num <= high:
                out.add(num)
            if num%10==9:
                dfs(num*10+8)
            elif num%10==0:
                dfs(num*10+1)
            else:
                dfs(num*10+num%10+1)
                dfs(num*10+num%10-1)
        for i in range(10):
            dfs(i)
        return sorted(list(out))
        