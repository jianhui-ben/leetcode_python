#917. Reverse Only Letters


#Given a string S, return the "reversed" string where all characters that 
#are not a letter stay in the same place, and all letters reverse their positions.

 

#Example 1:

#Input: "ab-cd"
#Output: "dc-ba"
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ## brute force
        l=[i for i in S if i.isalpha()]
        ans=''
        for i in range(len(S)):
            if S[i].isalpha():
                ans+=str(l.pop())
            else:
                ans+=S[i]
        assert not l
        return ans
        
