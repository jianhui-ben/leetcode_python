#969. Pancake Sorting

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ## divide and conquer
        self.out = []
        def recursion(arr, n):
            if n<2:
                return
            ## we need to put the largest of arr into the bottom or n th position
            i = arr.index(max(arr[:n]))
            if i== n-1:
                arr= arr[:i][::-1] + arr[i:]
                self.out.append(i+1)
                arr = arr[::-1]
                self.out.append(n)
            return recursion(arr, n-1)
            
        recursion(arr, len(arr))
        return self.out
        
