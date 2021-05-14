#659. Split Array into Consecutive Subsequences
#Given an integer array nums that is sorted in ascending order, return true if and only if you can split it into one or more subsequences such that each subsequence consists of consecutive integers and has a length of at least 3.

 

#Example 1:

#Input: nums = [1,2,3,3,4,5]
#Output: true
#Explanation:
#You can split them into two consecutive subsequences : 
#1, 2, 3
#3, 4, 5


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ## greedy algorithm
        ## O(n), O(n)
        
        ## traverse the nums:
        ## if attaching to the end: seq[num]-=1; seq[num+1]+=1; 
        ## if start a new sequence: stored[nums]/stored[nums+1]/ stored[nums+2] -=1, seq[nums+2]+=1
        ## else: false
        
        seq =  defaultdict(int)     ## key: last number of the existing sequence, value: counts of this last number
        stored = Counter(nums)   ### counter
        
        for num in nums:
            
            ## ignore the second and the third number of the new sequence created before
            if stored[num]==0:
                continue
            ## if attaching to the end
            if num-1 in seq and seq[num-1]>0:
                seq[num-1]-=1
                seq[num]+=1
                stored[num]-=1
                
            ## if start a new sequence
            elif num in stored and num+1 in stored and num+2 in stored and \
            stored[num]>0 and stored[num+1]>0 and stored[num+2]>0:
                seq[num+2]+=1
                stored[num]-=1
                stored[num+1]-=1
                stored[num+2]-=1
            else:
                return False
        return True
                
        
        
        
        