#216. Combination Sum III
#Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

#Note:

#All numbers will be positive integers.
#The solution set must not contain duplicate combinations.
#Example 1:

#Input: k = 3, n = 7
#Output: [[1,2,4]]
#Example 2:

#Input: k = 3, n = 9
#Output: [[1,2,6], [1,3,5], [2,3,4]]

##brute force:
from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]



class Solution:   
    ##DFS + backtracking time O(k), space O(k)
    ## time complexity: C(m, k)= C(9, k)= 9! / k! / (9-k)!
    ## space complexity: O(k+ k* # of ans)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def recursion(used, remain, next_num):
            if len(used)==k:
                if remain==0:
                    result.append(list(used))
                return 
            
            if next_num<= remain:
                for i in range(next_num, 10):
                    used.append(i)
                    recursion(used, remain-i, i+1)
                    used.pop()
        
        recursion([], n, 1)
        return result


## 2nd method: bit
## use a 9 bit binary string to represent a combination
## if the i-th bit is 1, then number (i+1) is used
## total # of 1s should be k
## time complexity: O(2^m) = O(2^9)
