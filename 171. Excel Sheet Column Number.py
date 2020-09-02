#171. Excel Sheet Column Number
#Given a column title as appear in an Excel sheet, return its corresponding column number.

#For example:

#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 
#    ...
#Example 1:

#Input: "A"
#Output: 1
#Example 2:

#Input: "AB"
#Output: 28


k='AB'
k.split()

ord('A')
##ord: A-Z: 65-90
class Solution:
    def titleToNumber(self, s: str) -> int:
        out=0
        if s is None or s=='': return 0
        for i in range(len(s)):
            c= len(s)-i-1
            out+=(ord(s[c])-64)*(26**i)
        return out

            