#1209. Remove All Adjacent Duplicates in String II
#You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

#We repeatedly make k duplicate removals on s until we no longer can.

#Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

#Example 1:

#Input: s = "abcd", k = 2
#Output: "abcd"
#Explanation: There's nothing to delete.
#Example 2:

#Input: s = "deeedbbcccbdaa", k = 3
#Output: "aa"
#Explanation: 
#First delete "eee" and "ccc", get "ddbbbdaa"
#Then delete "bbb", get "dddaa"
#Finally delete "ddd", get "aa"
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        stack
        """
        stack = []
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append((i, 1))
            else:
                stack.append((i, stack[-1][1] + 1))
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
                    
        return ''.join([letter for letter, _ in stack])
        
        
        
        
        """
        directly apply string
        time: O(n*k)
        space: O(k)
        """
#         out = ''
        
#         for i in s:
            
#             out += i
            
#             while len(out) >= k and out[-k:] == k * i:
#                 out = out[ : - k]
            
#         return out
                
        