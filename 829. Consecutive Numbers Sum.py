#829. Consecutive Numbers Sum
#Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

 

#Example 1:

#Input: n = 5
#Output: 2
#Explanation: 5 = 2 + 3
#Example 2:

#Input: n = 9
#Output: 3
#Explanation: 9 = 4 + 5 = 2 + 3 + 4
#Example 3:

#Input: n = 15
#Output: 4
#Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """
        we are looking for
        x + 1, x + 2, x+3 ... x + k
        the sum of the previous k numbers equal to n
        x*k + k*(1+k) / 2 = n
        2xk + k+K^2 = 2n
        k(2x + 1 + k)= 2n
        
        n = 5
        
        2n: 10
        
        1,2, 5, 10
        
        k = 1, 2x +k+1=10--> x = 4 --> [5]
        k = 2, 2x + k + 1 = 5 --> x = 1-->[2, 3]
        
        n=4, 2n=8
        1, 2, 4, 8
        k = 1, x = 3 --> [4]
        k = 2, x = 0.5 --> [1.5, 2.5]
        
        """
        out = 0
        for i in range(1, int((2*n)**0.5) + 1):            
        
            if 2 * n % i == 0:
                # x = (2 * n // i - 1 - i) / 2
                if (2 * n // i - 1 - i) / 2 % 1 == 0:
                    out += 1
        return out
            
        