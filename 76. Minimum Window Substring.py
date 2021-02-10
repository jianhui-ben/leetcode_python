#76. Minimum Window Substring
#Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

#Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

#Example 1:

#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"

class Solution:
    def check(self, dict_window, dict_t):
        for key, value in dict_t.items():
            if key not in dict_window or dict_window[key]<value:
                return False
        return True
    
    
    def minWindow(self, s: str, t: str) -> str:
        ##two pointers:
        if len(s)<len(t) or not t: return ""
        dict_t= dict(collections.Counter(t))
        right, left=len(t)-1, 0
        dict_window=dict(collections.Counter(s[:right+1]))
        out=None
        while right<len(s):
            if not self.check(dict_window, dict_t):
                right+=1
                if right<len(s) and s[right] not in dict_window:
                    dict_window[s[right]]=1
                elif right<len(s) and s[right] in dict_window: 
                    dict_window[s[right]]+=1
            else:
                if not out or right-left+1<= len(out):
                    out= s[left: right+1]
                left+=1
                if dict_window[s[left-1]]==1:
                    dict_window.pop(s[left-1])
                else:
                    dict_window[s[left-1]]-=1
        if not out: return ""
        return out


 ##approach 2:
     def minWindow(self, s: str, t: str) -> str:
        ##two pointers with improvements
        s_map=[(c, i) for i, c in enumerate(s) if c in t]
        filter_s= "".join([c for c in s if c in t])
        if len(filter_s)<len(t) or not t: return ""
        dict_t= dict(collections.Counter(t))
        right, left=len(t)-1, 0
        dict_window=dict(collections.Counter(filter_s[:right+1]))
        out=None
        while right<len(filter_s):
            if not self.check(dict_window, dict_t):
                right+=1
                if right<len(filter_s) and filter_s[right] not in dict_window:
                    dict_window[filter_s[right]]=1
                elif right<len(filter_s) and filter_s[right] in dict_window: 
                    dict_window[filter_s[right]]+=1
            else:
                if not out or s_map[right][1]-s_map[left][1]<= out[1]-out[0]:
                    out= (s_map[left][1], s_map[right][1])
                left+=1
                if dict_window[filter_s[left-1]]==1:
                    dict_window.pop(filter_s[left-1])
                else:
                    dict_window[filter_s[left-1]]-=1
        if not out: return ""
        left, right= out
        return s[left:right+1]