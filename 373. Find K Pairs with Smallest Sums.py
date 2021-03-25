#373. Find K Pairs with Smallest Sums
#You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

#Define a pair (u,v) which consists of one element from the first array and one element from the second array.

#Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

#Example 1:

#Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
#Output: [[1,2],[1,4],[1,6]] 
#Explanation: The first 3 pairs are returned from the sequence: 
#             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        ## minheap
        ## time O(k log N), O(k) space
        if not nums1 or not nums2: return []
        import heapq
        out=[]
        queue = [(nums1[0]+nums2[0], 0, 0)]
        visited= set()
        while queue and len(out)<k:
            _, i1,i2 = heapq.heappop(queue)
            out.append([nums1[i1],nums2[i2]])
            if i1+1<len(nums1) and (str(i1+1)+'_'+str(i2)) not in visited:
                heapq.heappush(queue, (nums1[i1+1]+nums2[i2], i1+1, i2))
                visited.add(str(i1+1)+'_'+str(i2))
            if i2+1<len(nums2) and (str(i1)+'_'+str(i2+1)) not in visited:
                heapq.heappush(queue, (nums1[i1]+nums2[i2+1], i1, i2+1))
                visited.add(str(i1)+'_'+str(i2+1))
        return out