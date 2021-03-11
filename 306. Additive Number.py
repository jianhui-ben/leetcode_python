#306. Additive Number
#Additive number is a string whose digits can form additive sequence.

#A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

#Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

#Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

#Example 1:

#Input: "112358"
#Output: true
#Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
#             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ##not typical backtracking:
        ## N**3
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                if (num[0]=='0' and i>1) or (num[i]=='0' and j-i>1):
                    continue
                    
                num1, num2 = int(num[:i]), int(num[i:j])
                while j< len(num):
                    num3 = num1+num2
                    if not num[j:].startswith(str(num3)):
                        break
                    j+=len(str(num3))
                    num1, num2 = num2, num3
                
                if j==len(num):
                    return True
        return False
