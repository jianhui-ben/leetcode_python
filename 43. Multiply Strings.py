#43. Multiply Strings

#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

#Example 1:

#Input: num1 = "2", num2 = "3"
#Output: "6"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ## two pointers on num1 and num2:
        
        res = [0] * (len(num1) +len(num2))
        
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i])*int(num2[j])
                temp = res[i+j+1]+ mul
                res[i+j+1] = temp%10
                res[i+j] += temp//10
                
        for i in range(len(res)):
            if res[i]!= 0:
                return ''.join([str(k) for k in res[i:]])
        return '0'