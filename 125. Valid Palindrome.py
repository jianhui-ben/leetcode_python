#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Note: For the purpose of this problem, we define empty string as valid palindrome.

#Example 1:

#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:

#Input: "race a car"
#Output: false


## recursion: time: O(n); space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def convert(str):
            if len(str)<=1: return True
            elif not str[0].isalpha() and not str[0].isnumeric():
                return convert(str[1:])
            elif not str[-1].isalpha() and not str[-1].isnumeric():
                return convert(str[:-1])
            elif str[0].lower()== str[-1].lower():
                return convert(str[1:-1])
            else: return False
        return convert(s)



## two pointer:
#space: O(1); time complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        head, tail= 0, len(s)-1
        while head<=tail:
            if not s[head].isalpha() and not s[head].isnumeric():
                head+=1
            elif not s[tail].isalpha() and not s[tail].isnumeric():
                tail-=1
            elif s[head].lower()==s[tail].lower():
                head+=1; tail-=1
            elif s[head].lower()!=s[tail].lower():
                return False
        return True
                