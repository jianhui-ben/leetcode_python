#674. Longest Continuous Increasing Subsequence


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ## stack
        if not nums: return 0
        stored = []
        out= float('-inf')
        for i in nums:
            if not stored or i<=stored[-1]:
                stored =[i]
            else:
                stored.append(i)
            out=max(len(stored), out)
            
            
        return out