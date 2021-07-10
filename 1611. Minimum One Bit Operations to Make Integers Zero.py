#1611. Minimum One Bit Operations to Make Integers Zero
#Given an integer n, you must transform it into 0 using the following operations any number of times:

#Change the rightmost (0th) bit in the binary representation of n.
#Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
#Return the minimum number of operations to transform n into 0.

 

#Example 1:

#Input: n = 0
#Output: 0
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        111  7 = 4 + 2 + 1
        110  6 = 4 + 2 + 0
        010  2 = 0 + 2 + 0
        011  3 = 0 + 2 + 1
        001  1 = 0 + 2 + 
        000  0
        
        10: 10->11->01->00: 3 steps
        100: 100->101->111->110->010.... 7 steps
        1000:1000 ->1001->1011->1010->1110 + 3 steps ->1100 -> 0100 + 7 steps 15 steps
        
        
        
        
        
        dp(1100) = 1 + dp(100)
        1110 = dp(10) + 1 + dp(100)
        
        """
        binval = (str(bin(n))[2:])
        n=len(binval)
        flag=False
        ans=0
        for i in range(n,0,-1):
            if not flag and binval[n-i]=='1':
                ans+=(2**i)-1
                flag=True
            elif flag and binval[n-i]=='1':
                ans-=(2**i)-1
                flag=False
        return(ans)