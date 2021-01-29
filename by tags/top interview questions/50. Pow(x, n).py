#50. Pow(x, n)
#Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

#Example 1:

#Input: x = 2.00000, n = 10
#Output: 1024.00000


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ## O(log n) time and space
        ## non-tail recursion
        temp_n= abs(n)
        def recur(n):
            if n==0: return 1
            if n==1: return x
            x1= recur(n//2)
            if n%2==0:
                return x1*x1
            else:
                return x1*x1*x
        if n>=0:
            return recur(temp_n)
        else:
            return 1/recur(temp_n)        
        ## need further thoughts
        # ## tail recursion
        # if n==0: return 1
        # temp_n= abs(n)
        # cur_prod=x
        # ans=1
        # while n>1:
        #     if n%2==1:
        #         ans*= cur_prod
        #     cur_prod*=cur_prod
        #     n/=2
        # return ans
            
       

        
        
        
        
        
        
        
#         ##bottom up brute force time O(n)
#         temp_n= abs(n)
#         out=1
#         for i in range(temp_n):
#             out*=x
#         if n<0:
#             return 1/out
#         return out
            
        
    
        
        
        
        
        
        