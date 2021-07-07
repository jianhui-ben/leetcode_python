#605. Can Place Flowers
#You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

#Example 1:

#Input: flowerbed = [1,0,0,0,1], n = 1
#Output: true
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        """
        from left to right, as long as a plot can be planted, we update the arr and
        decrement n
        as long as n is 0 or the num is finished traversing, return n == 0
        
        """
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        
        for i in range(len(flowerbed)):
            
            if n == 0:
                return True
            
            if flowerbed[i] == 0:
                
                ##left bound
                if i == 0 and len(flowerbed) > 1 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    
                ## right bound
                elif i == len(flowerbed) - 1 and len(flowerbed) > 1 \
                and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                
                ## middle
                elif 1 <= i <= len(flowerbed) - 2 and \
                flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            
            
        return n == 0
            
        
        