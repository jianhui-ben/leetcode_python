#1423. Maximum Points You Can Obtain from Cards
#There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

#In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

#Your score is the sum of the points of the cards you have taken.

#Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

#Example 1:

#Input: cardPoints = [1,2,3,4,5,6,1], k = 3
#Output: 12
#Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ## sliding window
        if k>=len(cardPoints): return sum(cardPoints)
        head, tail=cardPoints[:k], cardPoints[-k::]
        
        tot= head[::-1]+tail[::-1]
        left, right=0,0
        out, cum_sum=float('-inf'), 0
        while right<len(tot):
            cum_sum+=tot[right]
            right+=1
            while right-left>k:
                cum_sum-=tot[left]
                left+=1
            out=max(out, cum_sum)
        return out
            
            
            
        
