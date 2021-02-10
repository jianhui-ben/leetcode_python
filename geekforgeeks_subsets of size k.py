# https://aaronice.gitbook.io/lintcode/backtracking/subsets-of-size-k
    
# Input :   {1, 2, 3, 4}
#           k = 2
# Output :  1 2
#           1 3
#           1 4
#           2 3
#           2 4
#           3 4

## K recursions so O(k) space, O(k*n) time
def subset(sets, k):
    out= []
    l= list(sets)
    def dfs(left, idx, result):
        if len(result)==k:
            out.append(result)
            return
        if idx>len(left)-1: return
        for i in range(idx, len(left)):
            dfs(left, i+1, result+[left[i]])
    dfs(l, 0, [])
    return out

sets={1, 2, 3, 4, 5}
print(subset(sets, 4))

