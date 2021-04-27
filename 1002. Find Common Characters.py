#1002. Find Common Characters

#Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

#You may return the answer in any order.

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        stored = [Counter(name) for name in A]
        out=[]
        for char, _ in stored[0].items():
            min_ = min([counter.get(char, 0) for counter in stored])
            out+= [char]*min_
        
        return out
