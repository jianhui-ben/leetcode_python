#1963. Minimum Number of Swaps to Make the String Balanced
#You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

#A string is called balanced if and only if:

#It is the empty string, or
#It can be written as AB, where both A and B are balanced strings, or
#It can be written as [C], where C is a balanced string.
#You may swap the brackets at any two indices any number of times.

#Return the minimum number of swaps to make s balanced.

 

#Example 1:

#Input: s = "][]["
#Output: 1
#Explanation: You can make the string balanced by swapping index 0 with index 3.
#The resulting string is "[[]]".

class Solution:
    def minSwaps(self, s: str) -> int:
        
        cnt_open = 0
        
        for c in s:
            if c == '[':
                cnt_open += 1
            elif cnt_open > 0:
                cnt_open -= 1
        
        return (cnt_open + 1)//2
        
        