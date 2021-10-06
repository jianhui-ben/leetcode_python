#Lintcode 437: copy books

#Description
#Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

#These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

#They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

#Return the shortest time that the slowest copier spends.

#The sum of book pages is less than or equal to 2147483647

#Example
#Example 1:

#Input: pages = [3, 2, 4], k = 2
#Output: 5
#Explanation: 
#    First person spends 5 minutes to copy book 1 and book 2.
#    Second person spends 4 minutes to copy book 3.

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        
        if not pages: return 0
        
        tot_pages = sum(pages)
        left, right = tot_pages // k if not tot_pages % k else (tot_pages // k) + 1, tot_pages
        
        ## binary search to search for the last value which complete(pages, k, minute) return true
        def complete(pages, k, minute):
            ## 3, 2, 4
            ## cur_person: 3
            ## k: 2
            ## minute: 7

            cur_person = 0

            for page in pages:
                if page > minute:
                    return False
                if cur_person + page <= minute:
                    cur_person += page
                else:
                    k -= 1
                    cur_person = page
                if k < 0:
                    return False
            return k >= 1


        while left <= right:
            mid = left + (right - left) // 2
            if complete(pages, k, mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return max(left, 1)





        
