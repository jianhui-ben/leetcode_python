#1952. Three Divisors
#Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

#An integer m is a divisor of n if there exists an integer k such that n = k * m.

 

#Example 1:

#Input: n = 2
#Output: false
#Explantion: 2 has only two divisors: 1 and 2.
#Example 2:

#Input: n = 4
#Output: true
#Explantion: 4 has three divisors: 1, 2, and 4.
 

#Constraints:

#1 <= n <= 104
class Solution:
    def isThree(self, n: int) -> bool:
        """
        if the sqrt of n is a prime, then n is True
        """
        sqrt = int(n**0.5)

        if n != sqrt ** 2:
            return False
        
        def is_prime(n: int) -> bool:
            """Primality test using 6k+-1 optimization."""
            if n <= 3:
                return n > 1
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i ** 2 <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        return is_prime(sqrt)
    
        
        