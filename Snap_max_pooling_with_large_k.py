"""

“Max pooling for large windows”

Suppose you’re given a 2d matrix of integers and a positive integer k>= 1.
For every complete k*k window in that matrix, you want to compute and store the maximum value in that window.

Given a n*m integer matrix A and a positive integer k >= 1, return the max-pooled matrix of size (n - k + 1)*(m - k + 1).

Example:
k = 4
A = [
    [1, 2, 3],
    [5, 0, 0],
    [-1, -1, -1],
    [0, 5, 10]
]

Expected output:
[
    [5, 3],
    [5, 0],
    [5, 10]
]

"""

# ##
# [2, 3]
# [5, 0]
# [-1,-1]
# [5, 10]


# [2, 5, -1, 5]
# [3, 0, -1, 10]

# [5, 5, 5]
# [3, 0, 10]

# [5,3]
# [5, 0]
# [5, 10]

##


# def sliding_max(row, k):
#     if k>len(row):
#         return [max(row)]
#     out,temp=[], []
#     for i, val in enumerate(row):
#         if temp and temp[0]== i-k:
#             temp.pop(0)
#         while temp and row[temp[-1]]<val:
#             temp.pop()
#         temp.append(i)
#         out.append(row[temp[0]])
#     return out[k-1:]
# # test= [1,4,3,5]
# # k=5
# # print(sliding_max(test, k))


##time O(N^2+ M^2)
def max_pool(A, k):
    
    ##  [1,3,4,5], k=2, out [3,4,5]
    ##  in the temp, we can save the index of the maxmum value visited so far
    ## temp [4]
    if not A: return None
    hid, wid= len(A), len(A[0])
    if k>hid or k>wid:
        return None
    
    def sliding_max(row, k):
        if k>len(row):
            return [max(row)]
        out,temp=[], []
        for i, val in enumerate(row):
            if temp and temp[0]== i-k:
                temp.pop(0)
            while temp and row[temp[-1]]<val:
                temp.pop()
            temp.append(i)
            out.append(row[temp[0]])
        return out[k-1:]    
        
    out1=[]
    for row in A:
        out1.append(sliding_max(row, k))
        
    out1= [[row[i] for row in out1] for i in range(len(out1[0]))]
    # print(out1)
    out2=[]
    for row in out1:
        out2.append(sliding_max(row, k))
        
    return [[row[i] for row in out2] for i in range(len(out2[0]))]


k = 2
A = [
    [1, 2, 3],
    [5, 0, 0],
    [-1, -1, -1],
    [0, 5, 10]
]
      
print(max_pool(A, 3))
