#findShortestUniqueSubstring


## find shortest substring in arr which contain all unique characters
def findShortestUniqueSubstring(arr):
    ## sliding window: O(n), O(n)
    
    if not arr: return None
    stored=defaultdict(int)
    target = len(set(arr))
    left, right = 0, 0
    out=arr
    while right<len(arr):
        stored[arr[right]]+=1
        right+=1
        while len(stored)==target:
            if right-left<len(out):
                out = arr[left: right]
            if stored[arr[left]]==1:
                stored.pop(arr[left])
            else:
                stored[arr[left]]-=1
            left+=1
    return out
                
s='xyyzyzyx'
print(findShortestUniqueSubstring(s))

            
        
    
    