#91. Decode Ways

#A message containing letters from A-Z is being encoded to numbers using the following mapping:

#'A' -> 1
#'B' -> 2

#'Z' -> 26
#Given a non-empty string containing only digits, determine the total number 
#of ways to decode it.

#The answer is guaranteed to fit in a 32-bit integer.

 

#Example 1:

#Input: s = "12"
#Output: 2
#Explanation: It could be decoded as "AB" (1 2) or "L" (12).


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0 for x in range(len(s) + 1)] 
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(s)+1):
            if 0 < int(s[i-1:i]):
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]