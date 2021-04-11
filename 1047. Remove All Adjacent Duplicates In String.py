#1047. Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, S: str) -> str:
        ## stack
        
        stored = []
        for i in S:
            if not stored or stored[-1]!=i:
                stored.append(i)
            else:
                stored.pop()
        return ''.join(stored)
        
