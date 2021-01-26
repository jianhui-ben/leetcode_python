# all subsets of given size of a set
#Generate all possible subset of size r of the given array with distinct elements. 


s=set([1,2,3,4])
n= 2

def subsets_of_size_k(s, n):
    if n==0: return []
    out=[]
    s= list(s)
    def recur(cur, idx):
        if idx<= len(s):
            if len(cur)==n:
                out.append(cur)
            else:
                for next_idx in range(idx, len(s)):
                    recur(cur+[s[next_idx]], next_idx+1)
    recur([], 0)
    return out

print(subsets_of_size_k(s, n))