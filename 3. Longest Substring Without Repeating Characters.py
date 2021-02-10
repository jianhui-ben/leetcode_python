#3. Longest Substring Without Repeating Characters
#Given a string s, find the length of the longest substring without repeating characters.

 

#Example 1:

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.


class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     # hashset +dp time O(n2), space O(n)
    #     if len(s)<=1: return len(s)
    #     out=[]
    #     for i in range(len(s)):
    #         hashset = set()
    #         cur_max=0
    #         for k in range(i, len(s)):
    #             if s[k] in hashset:
    #                 out.append(cur_max)
    #                 break
    #             else:
    #                 hashset.add(s[k])
    #                 cur_max+=1
    #         out.append(cur_max)
    #     return max(out)
    
    
    ##sliding windows: need more time to think
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, out= 0, 0, 0
        stored={}
        while start<len(s) and end<len(s):
            if s[end] in stored:
                start= max(start, stored[s[end]])
            out= max(out, end-start+1)
            stored[s[end]]= end+1
            end+=1
        return out