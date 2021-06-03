#233. Number of Digit One
##Given an integer n, count the total number of digit 1 
#appearing in all non-negative integers less than or equal to n.
class Solution:
    def countDigitOne(self, n: int) -> int:
        ## interesting questions
        
        ## we go from the 1s to tens to hundreads
        str_n = str(n)
        m=len(str_n)
        count=0
        for i in range(1, m+1):
            head = n//int(10**i)
            tail = n%int(10**(i-1))
            count+=head *int(10**(i-1))
            if int(str_n[m-i])>1:
                count+=int(10**(i-1))
            elif int(str_n[m-i])==1:
                count+=tail+1
        return count
            
        
# 3,4,5, [X], 6,7
# we find how many numbers has X=1
# 1)
# 000     00
# 001     01
# 002     02
# ...     ..
# 344     99
# 345*100
# 2)  when x<1: 0
# 3)  when x>1:
#         00..99
#     1*100
# 4) when x==1:
#         00...67
#     1*68
        
        
        
        
        