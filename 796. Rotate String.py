796. Rotate String
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A)!= len(B): return False
        if not A: return True
        for _ in range(len(A)):
            A=A[1:] + A[0]
            if A==B:
                return True
            
        return False
