#438. Find All Anagrams in a String
#Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

#Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

#The order of output does not matter.

#Example 1:

#Input:
#s: "cbaebabacd" p: "abc"

#Output:
#[0, 6]


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        out=[]
        p_dict=dict(collections.Counter(p))
        window= dict(collections.Counter(s[:len(p)]))
        for start_i in range(len(s)-len(p)+1):
            # print(start_i)
            # print(window)
            if p_dict==window:
                out.append(start_i)
            if start_i+len(p)<len(s):
                first= s[start_i]
                if window[first]==1:
                    window.pop(first)
                else:
                    window[first]-=1
                last=s[start_i+len(p)]
                if last in window:
                    window[last]+=1
                else:
                    window[last]=1
        return out
            

        
        
        
        
        
        
        
        ##brute force
#         len_p=len(p)
#         sorted_p= ''.join(sorted([c for c in p]))
#         out=[]
#         for i in range(len(s)-len_p+1):
#             sub= ''.join(sorted([c for c in s[i: i+len_p]]))
#             if sub==sorted_p:
#                 out.append(i)
                
#         return out
            
            