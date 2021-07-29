#932. Beautiful Array
#An array nums of length n is beautiful if:

#nums is a permutation of the integers in the range [1, n].
#For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
#Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

 

#Example 1:

#Input: n = 4
#Output: [2,1,4,3]
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        mem = {1: [1]}
        def permutate(n):
            if n not in mem:
                odds, evens = permutate((n + 1) // 2), permutate((n) // 2)
                mem[n] = [i * 2 - 1 for i in odds] + [i * 2 for i in evens]
            return mem[n]
        
        return permutate(n)