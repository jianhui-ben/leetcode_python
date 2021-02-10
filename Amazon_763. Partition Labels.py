#763. Partition Labels

#A string S of lowercase English letters is given. We want to partition this string 
#into as many parts as possible so that each letter appears in at most one part, 
#and return a list of integers representing the size of these parts.

 

#Example 1:

#Input: S = "ababcbacadefegdehijhklij"
#Output: [9,7,8]
#Explanation:
#The partition is "ababcbaca", "defegde", "hijhklij".
#This is a partition so that each letter appears in at most one part.
#A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
#splits S into less parts.

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
 
        
        ##Ben's method
        if not S: return []
        out=[]
        ##save all the furthest index for every unique charater:
        furthest={}
        for i, v in enumerate(S):
            furthest[v]=i
        start_index=0    
        while start_index<len(S):
            temp_boundary= furthest[S[start_index]]
            cur_index=start_index
            while cur_index<temp_boundary:
                cur_index+=1
                temp_boundary=max(temp_boundary, furthest[S[cur_index]])
            out.append(cur_index-start_index+1)
            start_index=cur_index+1
            
        return out