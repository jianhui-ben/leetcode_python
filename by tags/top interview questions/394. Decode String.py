#394. Decode String
#Given an encoded string, return its decoded string.

#The encoding rule is: k[encoded_string], where the encoded_string inside the
#square brackets is being repeated exactly k times. Note that k is guaranteed to be
#a positive integer.

#You may assume that the input string is always valid; No extra white spaces, square
#brackets are well-formed, etc.

#Furthermore, you may assume that the original data does not contain any digits and
#that digits are only for those repeat numbers, k. For example, there won't be 
#input like 3a or 2[4].

class Solution:
    def decodeString(self, s: str) -> str:
        stack= []
        for i in s:
            if i!= ']':
                stack.append(i)
            else:
                letters, digits="", ""
                while stack[-1]!='[':
                    letters+= stack.pop()
                stack.pop()
                while stack and stack[-1].isdigit():
                    digits+=stack.pop()
                for i in range(int(digits[::-1])):
                    stack+= [l for l in letters[::-1]]
        return "".join(stack)
  
#         ##brute force
#         letters, digits, out= "","", ""
#         i=0
#         while i<len(s):
#             if s[i].isalpha():
#                 letters+=s[i]
#             elif s[i].isdigit():
#                 digits+=s[i]
#             elif s[i]=="[":
#                 stack= [s[i]]
#                 m=i+1
#                 while stack and m<len(s):
#                     if s[m]=='[':
#                         stack.append(s[m])
#                     elif s[m]==']':
#                         stack.pop()
#                     m+=1
    
#                 if not digits: times=0
#                 else: times= int(digits)
#                 rep=self.decodeString(s[i+1:m-1])
#                 for i in range(times):
#                     out+=rep
#                 return letters+out+self.decodeString(s[m:])
#             i+=1
#         return letters
 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
