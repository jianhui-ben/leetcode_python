#639. Decode Ways II

#A message containing letters from A-Z is being encoded to numbers using the following mapping way:

#'A' -> 1
#'B' -> 2

#'Z' -> 26
#Beyond that, now the encoded string can also contain the character '*', which can be 
#treated as one of the numbers from 1 to 9.

#Given the encoded message containing digits and the character '*', return the 
#total number of ways to decode it.

#Also, since the answer may be very large, you should return the output mod 109 + 7.

#Example 1:
#Input: "*"
#Output: 9
#Explanation: The encoded message can be decoded to the string: 
#    "A", "B", "C", "D", "E", "F", "G", "H", "I".

class Solution:
    def numDecodings(self, s: str) -> int:
        M=1000000007
        if not s or s[0]=='0': return 0
        dp= [0]* (len(s)+1)
        
        dp[0]= 1
        dp[1]=9 if s[0]=='*' else 1
        for i in range(1, len(s)):
            if s[i]=='*':
                dp[i+1]+= (9 *dp[i])% M
                if s[i-1]=='*':
                    dp[i+1]+=((26-10+1-2)*dp[i-1])% M
                elif int(s[i-1])>=1 and int(s[i-1])<=2:
                    ratio = 9 if int(s[i-1])==1 else 6
                    dp[i+1]+= (ratio *dp[i-1])% M
            else:
                if int(s[i])>0:
                    dp[i+1]+= dp[i]% M
                if s[i-1]=='*':
                    ratio = 2 if int(s[i])<=6 else 1
                    dp[i+1]+=(ratio*dp[i-1])% M
                elif int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<= 26:
                    dp[i+1]+=dp[i-1]% M
        return dp[-1]                