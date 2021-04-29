#354. Russian Doll Envelopes
#You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

#One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

#Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

#Note: You cannot rotate an envelope.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        ## sort and then dp find the longest increasing subsequence
        ## O(nlogn) time, O(N) space
        envelopes.sort(key =  lambda x: (x[0], -x[1]))
        limits = [h for w,h in envelopes]
        
        ## patience sorting
        top = [None]* len(limits)
        piles= 0
        for poker in limits:
            left, right=0, piles
            while left<right:
                mid = left+(right-left)//2
                if top[mid]<poker:
                    left=mid+1
                else:
                    right = mid
            
            if left==piles:
                piles+=1
            top[left]=poker
        return piles