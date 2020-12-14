#1090. Largest Values From Labels

#We have a set of items: the i-th item has value values[i] and label labels[i].

#Then, we choose a subset S of these items, such that:

#|S| <= num_wanted
#For every label L, the number of items in S with label L is <= use_limit.
#Return the largest possible sum of the subset S.

 

#Example 1:

#Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
#Output: 9
#Explanation: The subset chosen is the first, third, and fifth item.

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ## a maxheap and a hashmap to store the counts
        heap=[]
        for i in range(len(values)):
            heap.append((-values[i], labels[i]))
        heapq.heapify(heap)
        
        stored={}
        
        out=0
        cur_num=0
        while cur_num<num_wanted and heap:
            v, l= heapq.heappop(heap)
            if l not in stored:
                stored[l]=1
            elif stored[l]>=use_limit:
                continue
            else:
                stored[l]+=1
            out+=v
            cur_num+=1
        return -out
        