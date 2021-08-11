#132. Palindrome Partitioning II
#Given a string s, partition s such that every substring of the partition is a palindrome.

#Return the minimum cuts needed for a palindrome partitioning of s.

 

#Example 1:

#Input: s = "aab"
#Output: 1
#Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution:
    def minCut(self, s: str) -> int:
        
        """
        dp with middle expansion(genius method)
        O(n**2), O(n)
        """
        dp = [i for i in range(len(s))]
        
        
        def findMin(left, right, dp, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left == 0:
                    newCut = 0
                else:
                    newCut = dp[left - 1] + 1
                
                dp[right] = min(dp[right], newCut)
                
                left -= 1
                right += 1
                
        for mid in range(len(dp)):
            findMin(mid, mid, dp, s)
            findMin(mid - 1, mid, dp, s)
        
        return dp[-1]
        