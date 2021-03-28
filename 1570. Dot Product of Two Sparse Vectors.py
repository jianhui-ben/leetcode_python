1570. Dot Product of Two Sparse Vectors
class SparseVector:
    def __init__(self, nums: List[int]):
        ## dictionary(index: val)
        self.dic=collections.defaultdict(int)
        for i, v in enumerate(nums):
            if v!=0:
                self.dic[i]=v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        out=0
        for key, val in self.dic.items():
            if key in vec.dic:
                out+=val*vec.dic[key]
        return out
    ##if one is not sparse, we can just do 
        # for key, val in self.dic.items():
        #     out+=val*vec[key]
        
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)