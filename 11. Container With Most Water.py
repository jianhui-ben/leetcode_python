#11. Container With Most Water

#Given n non-negative integers a1, a2, ..., an , where each represents a point 
#at coordinate (i, ai). n vertical lines are drawn such that the two endpoints 
#of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
#forms a container, such that the container contains the most water.

#Note: You may not slant the container and n is at least 2.


class Solution:    
    def maxArea(self, height: List[int]) -> int:
        ## two pointers
        head, tail= 0, len(height)-1
        out=0
        while head!=tail:
            cur_height=min(height[head], height[tail])
            out= max(out, cur_height*(tail-head))
            if height[head]<= height[tail]:
                head+=1
            else: tail-=1
        return out
