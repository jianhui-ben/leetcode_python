#378. Kth Smallest Element in a Sorted Matrix
#Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

#Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ## binary search
        ## O(n) time
        start, end =  matrix[0][0], matrix[-1][-1]
        
        def count_less_or_equal(matrix, tar):
            count, smaller, larger= 0, matrix[0][0], matrix[-1][-1]
            r, c = len(matrix), len(matrix[0])
            i_r, i_c = r-1, 0
            while i_r>=0 and i_c<c:
                if matrix[i_r][i_c]<= tar:
                    smaller = max(smaller, matrix[i_r][i_c])
                    i_c+=1
                    count+=i_r+1
                else:
                    larger = min(larger, matrix[i_r][i_c])                    
                    i_r-=1

            return count, smaller, larger
        
        while start<end:
            mid = start+ (end - start)//2
            ## we want to track the smallest number bigger than mid and 
            ## largest number smaller or equal to mid
            count, smaller, larger= count_less_or_equal(matrix, mid)
            # print(start, end, mid, count, smaller, larger)
            if count==k:
                return smaller
            elif count<k:
                start =larger
            else:
                end = smaller
        return start
            
        
        
        
        
        # ## a better min heap approach:
        # ## time O(K(log n)), space O(N)
        # import heapq
        # queue = []
        # for r in range(len(matrix)):
        #     heapq.heappush(queue, (matrix[r][0], r, 0))
        # count =0
        # while True:
        #     num, r, c = heapq.heappop(queue)
        #     count+=1
        #     if count>=k: return num
        #     if c+1<len(matrix[0]):
        #         heapq.heappush(queue, (matrix[r][c+1], r, c+1))
        
        
        ## use min heap 
        ## time (k log n**2), space O(n**2)
        
#         import heapq
#         queue = [(matrix[0][0], 0,0)]
#         count =0
#         visited= set()
#         while True:
#             num, r, c = heapq.heappop(queue)
#             count+=1
#             if count>=k:
#                 return num
#             if r+1<len(matrix) and (str(r+1)+'_'+str(c)) not in visited:
#                 heapq.heappush(queue, (matrix[r+1][c],r+1, c))
#                 visited.add(str(r+1)+'_'+str(c))
#             if c+1<len(matrix[0]) and (str(r)+'_'+str(c+1)) not in visited:
#                 heapq.heappush(queue, (matrix[r][c+1],r, c+1))
#                 visited.add(str(r)+'_'+str(c+1))
        
        