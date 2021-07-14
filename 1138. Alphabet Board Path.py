#1138. Alphabet Board Path
#On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

#Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



#We may make the following moves:

#'U' moves our position up one row, if the position exists on the board;
#'D' moves our position down one row, if the position exists on the board;
#'L' moves our position left one column, if the position exists on the board;
#'R' moves our position right one column, if the position exists on the board;
#'!' adds the character board[r][c] at our current position (r, c) to the answer.
#(Here, the only positions that exist on the board are positions with letters on them.)

#Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

#Example 1:

#Input: target = "leet"
#Output: "DDR!UURRR!!DDD!"


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        out = ""
        
        def vertical_move(out, row1, row2):
            if row1 > row2:
                for _ in range(abs(row1 - row2)):
                    out += 'U'
            else:
                for _ in range(abs(row1 - row2)):
                    out += 'D'
            return out
        
        def horizontal_move(out, col1, col2):
            if col1 > col2:
                for _ in range(abs(col1 - col2)):
                    out += 'L'
            else:
                for _ in range(abs(col1 - col2)):
                    out += 'R'    
            return out
            
        
        def move_update(letter1, letter2):
            nonlocal out
            row1, col1 = (ord(letter1) - 97) // 5, (ord(letter1) - 97) % 5
            row2, col2 = (ord(letter2) - 97) // 5, (ord(letter2) - 97) % 5
            
            if ord(letter1) > ord(letter2):
                out = vertical_move(out, row1, row2)
                out = horizontal_move(out, col1, col2)
            else:
                out = horizontal_move(out, col1, col2)
                out = vertical_move(out, row1, row2)

            out += '!'
            return
            
        
        for i in range(len(target)):
            
            if i == 0:
                move_update('a', target[i])
            else:
                move_update(target[i - 1], target[i])
        
        return out
        