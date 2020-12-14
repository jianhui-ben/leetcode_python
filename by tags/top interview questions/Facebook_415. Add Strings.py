#415. Add Strings
#Given two non-negative integers num1 and num2 represented as string, 
#return the sum of num1 and num2.

#Note:

#The length of both num1 and num2 is < 5100.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l_num1, l_num2= num1[::-1], num2[::-1]
        while len(l_num1)!=len(l_num2):
            if len(l_num1)<len(l_num2):
                l_num1+='0'
            else:
                l_num2+='0'
        final=''
        carry_over=0
        for i in range(len(l_num1)):
            result= int(l_num1[i])+int(l_num2[i])+carry_over
            if result>9:
                final+=str(result)[-1]
                carry_over=1
            else:
                final+=str(result)
                carry_over=0
        if carry_over==1:
            final+='1'
        return final[::-1]
        