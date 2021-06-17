#1105. Filling Bookcase Shelves
#We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

#We want to place these books in order onto bookcase shelves that have total width shelf_width.

#We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

#Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

#Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
#https://leetcode.com/problems/filling-bookcase-shelves/

# Similar Problems: 300, 673, 368, 1105


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        
        mem = defaultdict(int)
        
        def dfs(thickness, book_idx, level_height):
            
            ## return the height of level and below level
            
            nonlocal mem
            nonlocal books
            nonlocal shelf_width
            if book_idx == len(books):
                return level_height

            if (thickness, book_idx, level_height) in mem:
                 return mem[(thickness, book_idx, level_height)]

            cur_book = books[book_idx]

              ## if there's no books on the current level of the shelf
            if thickness == 0:
                result_height= dfs(cur_book[0], book_idx +1, max(level_height, cur_book[1]))


            elif thickness + cur_book[0] > shelf_width:
                result_height =  level_height + dfs(0, book_idx, 0)

            else:
                result_height = min(dfs(thickness + cur_book[0], book_idx+ 1, max(level_height, cur_book[1])), \
                                level_height + dfs(0, book_idx, 0))

            mem[(thickness, book_idx, level_height)] = result_height

            return result_height
    
        out = dfs(0, 0, books[0][1])
        # print(mem)
        return out
        
        
        
#         """
#         status: book_id
#         choice: current level,  next level
#         dp[i]: the min height of books[:i+1]
#         time O(N**2), O(N) space
#         """
        
#         dp = [float('inf')] * len(books)
#         dp[0] = books[0][1]
#         for i in range(1, len(dp)):
#             cur_width = 0
#             max_height = float('-inf')
#             for j in range(i, -1, -1):  ## check sumwidth(j+1.. i)<= shelf_width
#                 if cur_width + books[j][0] <= shelf_width:
#                     max_height = max(max_height, books[j][1])
#                     cur_width += books[j][0]
#                     dp[i] = min(dp[i], (dp[j-1] if j>0 else 0) + max_height)
#                 else:
#                     break
                    
#         return dp[-1]
            
        
        
        
          

        
        
        