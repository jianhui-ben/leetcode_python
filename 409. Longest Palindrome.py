#409. Longest Palindrome
#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

#Example 1:

#Input: s = "abccccdd"
#Output: 7
#Explanation:
#One longest palindrome that can be built is "dccaccd", whose length is 7.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for c, fre in Counter(s).items():
            ans += fre if not fre % 2 else fre - 1
        
        return ans if ans == len(s) else ans + 1
            
            