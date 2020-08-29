#67. Add Binary
#Given two binary strings, return their sum (also a binary string).

#The input strings are both non-empty and contains only characters 1 or 0.

#Example 1:

#Input: a = "11", b = "1"
#Output: "100"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        l_a, l_b= list(a)[::-1], list(b)[::-1]
        while len(l_a) !=len(l_b):
            if len(l_a)>len(l_b):
                l_b.append('0')
            else:
                l_a.append('0')
                
        final_bi=[]
        carry_over=0
        for i in range(len(l_a)):
            s=int(l_a[i])+int(l_b[i])+carry_over
            if s<=1:
                final_bi.append(str(s))
                carry_over=0
            elif s==2:
                final_bi.append('0')
                carry_over=1
            else:
                final_bi.append('1')
                carry_over=1
        
        if carry_over==1:
            final_bi.append('1')
        ans=''
        for i in final_bi:
            ans+=i
            
        return ans[::-1]
                