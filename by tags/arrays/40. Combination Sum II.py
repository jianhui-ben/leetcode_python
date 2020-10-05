#40. Combination Sum II
#Given a collection of candidate numbers (candidates) and a target number (target), 
#find all unique combinations in candidates where the candidate numbers sums to target.

#Each number in candidates may only be used once in the combination.

#Note:

#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#Example 1:

#Input: candidates = [10,1,2,7,6,1,5], target = 8,
#A solution set is:
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out=[]
        candidates.sort()
        if len(candidates)==0 or target< candidates[0] or target> sum(candidates):
            return  []
        
        def dfs(stored, start_index, target):
            if target==0:
                out.append(list(stored))
            
            for i in range(start_index, len(candidates)):
                if target<candidates[i]:
                    break
                if i!=start_index and candidates[i]==candidates[i-1]:
                    continue
                stored.append(candidates[i])
                dfs(stored, i+1, target- candidates[i])
                stored.pop()
            
        dfs([], 0, target)
        return out