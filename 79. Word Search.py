#79. Word Search
#Given an m x n board and a word, find if the word exists in the grid.

#The word can be constructed from letters of sequentially adjacent cells, 
#where "adjacent" cells are horizontally or vertically neighboring. 
#The same letter cell may not be used more than once.

#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#Output: true

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column]==word[0] and self.search(row, column, board, 0, word):
                    return True
        return False
    
    def search(self, row, column, board, index, word):
        if index==len(word):
            return True
        if row<0 or row>= len(board) \
            or column<0 or column>=len(board[0]) \
            or board[row][column]!=word[index]:
            return False
        temp= board[row][column]
        board[row][column]="" ## hide the current one
        found= self.search(row+1, column, board, index+1, word) or self.search(row, column+1, board, index+1, word) or self.search(row-1, column, board, index+1, word) or self.search(row, column-1, board, index+1, word)
        board[row][column]= temp
        return found
