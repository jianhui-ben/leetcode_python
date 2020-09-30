#39. Combination Sum
#Given a set of candidate numbers (candidates) (without duplicates) and 
#a target number (target), find all unique combinations in candidates where 
#the candidate numbers sums to target.

#The same repeated number may be chosen from candidates unlimited number of times.

#Note:

#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#Example 1:

#Input: candidates = [2,3,6,7], target = 7,
#A solution set is:
#[
#  [7],
#  [2,2,3]
#]

##depth first search:

# time O(h*n); space O(h*# of answers);
def combinationSum(candidates, target):
    result=[]
    candidates.sort()
    if len(candidates)==0 or candidates[0]>target: return []


    def depth_first(stored, head, tar):
        if tar==0:
            result.append(list(stored))
        for i in range(head, len(candidates)):
            if tar< candidates[i]: 
                break
            stored.append(candidates[i])
            depth_first(stored, i, tar-candidates[i])
            stored.pop()
    depth_first([], 0, target)
    result= list(set(tuple(a) for a in result))
    return result

candidates=[2,3,6,7]
target=7

combinationSum(candidates, target)  

