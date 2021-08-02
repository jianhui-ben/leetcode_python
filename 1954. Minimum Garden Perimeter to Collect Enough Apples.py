#1954. Minimum Garden Perimeter to Collect Enough Apples
#In a garden represented as an infinite 2D grid, there is an apple tree planted at every integer coordinate. The apple tree planted at an integer coordinate (i, j) has |i| + |j| apples growing on it.

#You will buy an axis-aligned square plot of land that is centered at (0, 0).

#Given an integer neededApples, return the minimum perimeter of a plot such that at least neededApples apples are inside or on the perimeter of that plot.

#The value of |x| is defined as:

#x if x >= 0
#-x if x < 0


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        
        """
        side length: 1; perimeter: 1* 8; apples: (1 + 2) * 4 = 3* 4
        side length: 2: perimeter: 2* 8; apples: (1 + 2) * 4 + (3 + 2+ 3) * 4 + 4 * 4 = 15 * 4
        side length: 3: perimeter: 3* 8; apples: 15 * 4 +  (5 + 4 + 3 + 4 + 5) * 4 + 6 * 4 = 42 * 4
        side length: 4: perimeter: 4* 8; apples: 42 * 4 + (5 + 6 + 7) * 8 + (4 + 8) * 4
        
        """
        half_side_len = 1
        apples = 12
        
        while apples < neededApples:
            
            half_side_len += 1
            
            apples += (half_side_len * 3) * (half_side_len - 1) * 4 + half_side_len * 12
            
        return 8 * half_side_len