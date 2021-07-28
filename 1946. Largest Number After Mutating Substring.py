#1946. Largest Number After Mutating Substring
#You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. More formally, digit d maps to digit change[d].

#You may choose to mutate any substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).

#Return a string representing the largest possible integer after mutating (or choosing not to) any substring of num.

#A substring is a contiguous sequence of characters within the string.

 

#Example 1:

#Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
#Output: "832"
#Explanation: Replace the substring "1":
#- 1 maps to change[1] = 8.
#Thus, "132" becomes "832".
#"832" is the largest number that can be created, so return it.


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        

        s = ''        
        for i, val in enumerate(num):
            if change[int(val)] > int(val):
                s += str(change[int(val)])
                break
            else:
                s += num[i]
        
        
        
        for i, val in enumerate(num[i + 1:], i + 1):
            
            if change[int(val)] >= int(val):
                s += str(change[int(val)])
            else:
                s += num[i:]
                break
            # print(s)
        return s
                