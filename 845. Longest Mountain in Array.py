#845. Longest Mountain in Array

#You may recall that an array arr is a mountain array if and only if:

#arr.length >= 3
#There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ## two pointer can reduce the space to O(1)
        left=0
        self.out = 0
        while left<len(arr):
            ## look for the peak
            right=left
            if right+1<len(arr) and arr[right+1]> arr[right]:
                while right+1<len(arr) and arr[right+1]> arr[right]:
                    right+=1
                    
                if right+1<len(arr) and arr[right+1]< arr[right]:
                    while right+1<len(arr) and arr[right+1]< arr[right]:
                        right+=1
                    self.out=max(self.out, right-left+1)
            left = max(right, left+1)
        return self.out

        
        
        ## two pass
        ## O(n), O(n)
        def traverse(arr):
            temp=[]
            for i in range(len(arr)):
                if not temp or arr[i]<=arr[i-1]:
                    temp.append(0)
                else:
                    temp.append(temp[-1]+1)
            return temp

        l_to_r, r_to_l = traverse(arr), traverse(arr[::-1])[::-1]
        self.out = float('-inf')
        for i in range(len(l_to_r)):
            if l_to_r[i]>0 and r_to_l[i]>0:
                self.out=max(self.out, l_to_r[i]+r_to_l[i])
        if self.out== float('-inf'): return 0
        else: return self.out+1
        