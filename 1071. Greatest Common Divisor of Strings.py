#1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        ## from largest prefix to the shortest one
        ## O(N) approximately , O(1)
        
        ## make str1 shorter
        if len(str1)>len(str2):
            str1, str2 = str2, str1
        
        
        def divisible(string, cur_selection):
            if len(string)%len(cur_selection)!=0: return False
            for start_i in range(0, len(string), len(cur_selection)):
                if string[start_i:start_i+len(cur_selection)]!= cur_selection:
                    return False
            return True
        
        
        for i in range(len(str1), 0, -1):
            cur_selection = str1[:i]
            if divisible(str1, cur_selection) and divisible(str2, cur_selection):
                return cur_selection
        
        
        return ""
        
