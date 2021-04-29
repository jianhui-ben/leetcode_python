#72. Edit Distance
#Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

#You have the following three operations permitted on a word:

#Insert a character
#Delete a character
#Replace a character
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ## status: i and j for word1 and word2; 1<=i<=len(word1)
        ## choice: I could choose to insert/delete vs replace
        ## O(M*N), space O(M*N
        
        dp = [[None for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for row in range(len(dp)):
            for col in range(len(dp[row])):
                if row==0 or col ==0:
                    dp[row][col]=max(row, col)
                else:
                    if word1[row-1]==word2[col-1]:
                        dp[row][col] = dp[row-1][col-1]
                    else:
                        dp[row][col] = min(1+dp[row-1][col-1], 1+dp[row-1][col],\
                                          1+dp[row][col-1])
        return dp[len(word1)][len(word2)]
        