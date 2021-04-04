#395. Longest Substring with At Least K Repeating Characters
#Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

#Example 1:

#Input: s = "aaabb", k = 3
#Output: 3
#Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        ## interesting sliding window solution:
        ## we need to determine how many unique chara in our substring
        ## time O(N), space: O(1)
        cnt=0
        for _, fre in Counter(s).items():
            if fre>= k:
                cnt+=1
        if cnt==0: return 0
        out=[]
        
        def check(window):
            for _, fre in window.items():
                if fre<k: return False
            return True
        
        for i in range(1, cnt+1):
            ## sliding window to get the longest substring containing i unique chara
            left, right= 0, 0
            window=defaultdict(int)
            longest= 0
            while right<len(s):
                window[s[right]]+=1
                right+=1
                while len(window)>i:
                    if window[s[left]]==1: window.pop(s[left])
                    else: window[s[left]]-=1
                    left+=1
                
                if check(window):
                    longest=max(longest, right-left)
            out.append(longest)
        return max(out)