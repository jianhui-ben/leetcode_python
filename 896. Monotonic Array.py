#896. Monotonic Array


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        ## traverse forward and backward twice:
        ## O(n), O(1)
        def is_increasing(arr):
            if len(arr)<=1: return True
            for i in range(1, len(arr)):
                if arr[i]<arr[i-1]:
                    return False
            return True
        
        if not is_increasing(A) and not is_increasing(A[::-1]):
            return False
        return True
