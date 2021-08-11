#926. Flip String to Monotone Increasing
#A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

#You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

#Return the minimum number of flips to make s monotone increasing.

 

#Example 1:

#Input: s = "00110"
#Output: 1
#Explanation: We flip the last digit to get 00111.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        get total sum to be sum_
        
        
        "00011000"
         ^
        sum_ = 2
        cum_sum = 0
        out = 7
        
        Time: O(n)
        space: O(1)
        """
        
        sum_ = 0 
        for i in s:
            sum_ += int(i)
        
        cum_sum, out = 0, len(s) - 1
        for i, c in enumerate(s):
            ## consider i as the first 1
            out = min(out, cum_sum + len(s) - i - (sum_ - cum_sum))
            cum_sum += int(c)
            
        return min(out, sum_) 
        