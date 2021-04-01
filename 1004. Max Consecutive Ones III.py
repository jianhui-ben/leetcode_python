#1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ##sliding window
        ## O(n), space O(1)
        left, right=0, 0
        out= K
        cnt=0
        while right<len(A):
            if A[right]==1:
                right+=1
            elif A[right]==0 and cnt<K:
                cnt+=1
                right+=1
            else:
                while A[left]==1:
                    left+=1
                left+=1
                cnt-=1
            out=max(out, right-left)
        return out
                
                    
