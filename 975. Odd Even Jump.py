#975. Odd Even Jump
#You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

#You may jump forward from index i to index j (with i < j) in the following way:

#During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
#During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
#It may be the case that for some index i, there are no legal jumps.
#A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

#Return the number of good starting indices.

 

#Example 1:

#Input: arr = [10,13,12,14,15]
#Output: 2
#Explanation: 
#From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
#From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
#From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
#From starting index i = 4, we have reached the end already.
#In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
#jumps.

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        """
        input: list of integers (>=0), len(input) >= 1
        output: int: # of good start point to reach to the end


        at any index i, if it's a even jump: j is constant, if it's a odd jump: j is also constant

        status: position i, current jump is a odd / even jump

        [10,13,12,14,15]
          ^
        max_smaller: 12
        min_greater: 14

        [10,12,13,14,15]


        [10,13,12,14,15]

        [(10, 0), (12, 2), (13, 1), (14, 3), (15, 4)]
        ^                         target


        index 0: (index 2) odd
        index 2:  (index 3) odd
        index 1: (index 3) odd

        induction function:
        min_greater, max_smaller
        if next_jump[cur_idx][odd] exist:
          dp[current_idex][odd] = dp[next_jump[cur_idx][odd]][even]
        else:
          dp[current_idex][odd] = False



        if next_jump[cur_idx][even] exist:
          dp[current_idex][even] = dp[next_jump[cur_idx][even]][odd]
        else:
          dp[current_idex][even] = False


        time: O(Nlogn)
        space: O(n)

        """

        ## next_jump[i][0]: from position i, if it's a odd jump, return its next position
        next_jump = [[None for _ in range(2)] for _ in range(len(arr))] 

        index_arr = [(val, i) for i, val in enumerate(arr)]
        index_arr.sort(key = lambda x: (x[0], x[1]))

        # (10, 0), (12, 2), (13, 1), (14, 3), (15, 4)] 
        stack = []
        for _, idx in index_arr:
            while stack and stack[-1] <= idx:
                cur_idx = stack.pop()
                next_jump[cur_idx][0] = idx
            stack.append(idx)
        # print(index_arr, ' ', next_jump)
            
        
        stack = []
        index_arr.sort(key = lambda x: (-x[0], x[1]))
        
        for _, idx in index_arr:
            while stack and stack[-1] < idx:
                cur_idx = stack.pop()
                next_jump[cur_idx][1] = idx
            stack.append(idx)

        # print(" ")
        # print(index_arr, " ", next_jump)
        
        dp = [[None for _ in range(2)] for _ in range(len(arr))]
        dp[-1][0], dp[-1][1] = True, True

        for cur_idx in range(len(dp) - 2, -1, -1):
            for is_even in range(2):
                if next_jump[cur_idx][is_even] != None:
                    dp[cur_idx][is_even] = dp[next_jump[cur_idx][is_even]][1 - is_even]
                else:
                    dp[cur_idx][is_even] = False

        cnt = 0
        for odd_to_end, _ in dp:
            if odd_to_end:
                cnt += 1

        return cnt        