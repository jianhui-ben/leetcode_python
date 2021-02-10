#1239. Maximum Length of a Concatenated String with Unique Characters


#Given an array of strings arr. String s is a concatenation of a sub-sequence 
#of arr which have unique characters.

#Return the maximum possible length of s.

 

#Example 1:

#Input: arr = ["un","iq","ue"]
#Output: 4
#Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
#Maximum length is 4.


class Solution:
    ##method 1: python backtracking
    def dfs(self, arr, string):
        if len(set(string))==len(string):
            self.max= max(self.max, len(string))
        else:
            return self.max
        for i, c in enumerate(arr):
            self.dfs(arr[i:], string+c)
        return self.max
    
    def maxLength(self, arr: List[str]) -> int:
        self.max=0
        return self.dfs(arr, "")
    

#     ## method2 :time O(2**N) space O(N)
#     def unique_counts(self, string):
#         l= len(set(string))
#         if l == len(string):
#             return l
#         else: return -1

#     def maxLength(self, arr: List[str]) -> int:
#         ##dfs to create all the combinations
#         self.out= 0
#         def dfs(arr, index, cur_string):
#             temp=self.unique_counts(cur_string)
#             if temp>self.out:
#                 self.out= temp
#             if index==len(arr):
#                 return
#             dfs(arr, index+1, cur_string)
#             dfs(arr, index+1, cur_string+arr[index])
        
#         dfs(arr,0,"")
#         return self.out
    
        
        
        
                    
        
        
                    