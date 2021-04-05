#733. Flood Fill


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
 

        ## typical dfs:
        ## time complexity O(n), space O(n)
        if newColor==image[sr][sc]: 
                return image
        
        def fill(sr,sc, new, old):
            if sr>=0 and sr< len(image) and sc>=0 and sc<len(image[0]):
                if image[sr][sc]==old:
                    image[sr][sc]=new
                    fill(sr+1,sc, new, old)
                    fill(sr-1,sc, new, old)
                    fill(sr,sc+1, new, old)
                    fill(sr,sc-1, new, old)
        
        fill(sr,sc, newColor, image[sr][sc])
        return image
        
