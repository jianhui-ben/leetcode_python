##1640. Check Array Formation Through Concatenation
#You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

#Return true if it is possible to form the array arr from pieces. Otherwise, return false.

 

#Example 1:

#Input: arr = [85], pieces = [[85]]
#Output: true

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        ## using the hashmap and that numbers in pieces are distinct
        ## O(n), O(n)
        stored = defaultdict()
        for l in pieces:
            stored[l[0]] = l
        i= 0
        while i<len(arr):
            if arr[i] not in stored:
                return False
            
            one_piece = stored[arr[i]]
            if len(arr)-i>=len(one_piece) and arr[i:i+len(one_piece)]==one_piece:
                i+=len(one_piece)
            else:
                return False
        return True
        
        
        
        
        ## a more general situation where number in pieces are not distinct
        ## O(N**2), O(n)
        ## convert list into a string
        target = '_'.join([str(i) for i in arr])
        small_pieces = ['_'.join([str(i) for i in k]) for k in pieces]
        visited = set()
        
        def dfs(target, small_pieces, visited):
            if not target:
                return True
            if target[0]=='_':
                target = target[1:]
            for one_piece in small_pieces:
                if one_piece not in visited\
                and len(target)>= len(one_piece) \
                and target[:len(one_piece)]==one_piece:
                    visited.add(one_piece)
                    res = dfs(target[len(one_piece):], small_pieces, visited)
                    if res:
                        return True
                    visited.remove(one_piece)
            return False

        return dfs(target, small_pieces, visited)
        