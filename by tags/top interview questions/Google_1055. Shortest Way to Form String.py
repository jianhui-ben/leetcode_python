#1055. Shortest Way to Form String

#From any string, we can form a subsequence
#of that string by deleting some number of characters (possibly no deletions).

#Given two strings source and target, return the minimum number
#of subsequences of source such that their concatenation equals target. 
#If the task is impossible, return -1.

 

#Example 1:

#Input: source = "abc", target = "abcbc"
#Output: 2
#Explanation: The target "abcbc" can be formed by "abc" and "bc", 
#which are subsequences of source "abc".


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t,s=set(target), set(source)
        for i in t:
            if i not in s: return -1
        
        i_target, out=0, 0
        while i_target<len(target):
            i_source=0
            while i_source<len(source):
                if target[i_target]==source[i_source]:
                    i_target+=1
                    if i_target==len(target): return out+1
                i_source+=1
            out+=1

