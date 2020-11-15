#424. Longest Repeating Character Replacement

#Given a string s that consists of only uppercase English letters, you 
#can perform at most k operations on that string.

#In one operation, you can choose any character of the string and change 
#it to any other uppercase English character.

#Find the length of the longest sub-string containing all repeating letters 
#you can get after performing the above operations.

#Note:
#Both the string's length and k will not exceed 104.

#Example 1:

#Input:
#s = "ABAB", k = 2

#Output:
#4

#Explanation:
#Replace the two 'A's with two 'B's or vice versa.


class Solution:
    ## time limit exceeded: O(n2) and O(n)
    # def characterReplacement(self, s: str, k: int) -> int:
        # if len(s)<=1:return len(s)
        # dp= [None]* (len(s))
        # for i in range(len(s)):
        #     cur_index, cur_longest, changes= i, 0,  k
        #     while cur_index<len(s):
        #         if s[cur_index]== s[i]:
        #             cur_longest+=1
        #             cur_index+=1
        #         elif changes>0:
        #             cur_longest+=1
        #             cur_index+=1
        #             changes-=1
        #         else: break
        #     dp[i]= min(cur_longest+changes, len(s))
        # return max(dp)
        
    # slicing windows O(n), space O(# of unique numbers)
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)<=1:return len(s)
        start, end, out= 0, 0, 0
        collect={}
        while start< len(s) and end<len(s):
            if s[end] in collect:
                collect[s[end]] +=1
            else: collect[s[end]]=1
            if end-start+1 - max(collect.values())> k:
                collect[s[start]]-=1
                start+=1
            out=max(out, end-start+1)
            end+=1
        return out