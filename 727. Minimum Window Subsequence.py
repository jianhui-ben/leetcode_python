#727. Minimum Window Subsequence
#Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

#If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        ## two pointer forward and backward
        ## Time O(len(S) * len(T)), space O(1)
        i= 0
        out= S+'a'
        
        def forward(s, t, i):
            i_s, i_t=i, 0
            while i_s<len(s):
                if s[i_s]==t[i_t]:
                    i_t+=1
                i_s+=1
                if i_t>=len(t):
                    return i_s-1
            return None
        
        def backward(s, t, i):
            i_s, i_t=i, len(t)-1
            while i_s>-1:
                if s[i_s]==t[i_t]:
                    i_t-=1
                i_s-=1
                if i_t<0:
                    return i_s+1
            return None
        
        while i<len(S):
            i_s_end= forward(S, T, i) ## return 4
            if i_s_end: 
                i_s_start= backward(S, T, i_s_end) ## return 1
                if  i_s_end-i_s_start+1<len(out):
                    out=S[i_s_start:i_s_end+1]
                i= i_s_start+1
            else:
                break
        
        return out if out!= S+'a' else ""
            
            
            
            
            
        
        
        
        
        
        
#         ## sliding window + ordered dict
#         left, right, min_dis, out =0, 0, float('inf'), (None, None)
        
#         def check(S, left, right, T):
#                 if right-left<len(T): return False
#                 s_i, t_i= left, 0
#                 while t_i<len(T):
#                     if s_i>=right:
#                         return False
#                     if S[s_i]==T[t_i]:
#                         t_i+=1
#                     s_i+=1
#                 return True

#         while right<len(S):
#             right+=1
#             # print(left, right)
#             while check(S, left, right, T):
#                 if right-left<min_dis:
#                     min_dis=right-left
#                     out=(left, right)
#                 left+=1
#         if out==(None, None): return ""
#         else: return S[out[0]:out[1]]
                            
        
        