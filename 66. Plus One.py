#Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

#The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contains a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.

#Example 1:

#Input: [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Example 2:

#Input: [4,3,2,1]
#Output: [4,3,2,2]
#Explanation: The array represents the integer 4321.


def plusOne(digits):
    if digits==[]:
        return [1]
    last_digit= digits[-1]
    if last_digit<9:
        x=digits[-1]+1
        return digits[:-1]+ [x]
    return plusOne(digits[:-1])+[0]

plusOne([1,9,9])  ## [2,0, 0]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        out=[]
        added=False
        for i in digits[::-1]:
            if not added:
                if i<9:
                    out.insert(0,  i+1)
                    added= True
                else: out.insert(0, 0)
            else: out.insert(0, i)
        if not added:
            out.insert(0, 1)
            
        return out
            