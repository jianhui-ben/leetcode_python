1130. Minimum Cost Tree From Leaf Values


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        ## divide arr into arr[:i] and arr[i:] for i in [1:len(arr)-1]
        # O(n**3) time limit exceeded
        self.mem =defaultdict(int)
        
        def recursion(arr, start, end):
            if end-start<=0: return 0
            if (start, end) in self.mem: return self.mem[(start, end)]
            min_out = float('inf')
            for i in range(start, end):
                l_sum= recursion(arr, start, i)
                r_sum =recursion(arr, i+1, end)
                
                min_out=min(min_out, l_sum+r_sum+max(arr[start:i+1])*max(arr[i+1:end+1]))
            
            self.mem[(start, end)] = min_out
            
            return min_out
        
        return recursion(arr, 0, len(arr)-1)
    
    
#         def mctFromLeafValues_one(arr):
#             ## two pointer maybe doest't work here 
#             if not arr or len(arr)==1: return 0
#             if len(arr)==2: 
#                 return arr[0]*arr[1]
#             from collections import deque
#             non_leaf=[]
#             arr= deque(arr)
#             while len(arr)>2:
#                 v1, v2, v3 = arr.popleft(), arr.popleft(), arr.popleft()
#                 if v1 * v2<= v2*v3:
#                     non_leaf.append(v1 * v2)
#                     arr.appendleft(v3)
#                     arr.appendleft(max(v1, v2))
#                 else:
#                     non_leaf.append(v2*v3)
#                     arr.appendleft(max(v2, v3))
#                     arr.appendleft(v1)
#             return sum(non_leaf)+ arr[0]*arr[1]
#         return min(mctFromLeafValues_one(arr), mctFromLeafValues_one(arr[::-1]))
            
        
