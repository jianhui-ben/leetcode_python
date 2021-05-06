#1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

#Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        ## O(nlogn), O(n) space
        horizontalCuts.sort()
        verticalCuts.sort()
        
        def get_max(range_, cuts, cur_max):
            start, end = range_
            if not cuts:
                return max(end-start, cur_max)
            cut = cuts[0]
            if cut-start>= end-cut:
                return max(cut-start, cur_max)
            cur_max = max(cur_max, cut-start)
            cuts.pop(0)
            return get_max((cut, end), cuts, cur_max)
        return  (get_max((0, h), horizontalCuts, float('-inf')) * \
        get_max((0,w), verticalCuts, float('-inf')))%(10**9 + 7)
