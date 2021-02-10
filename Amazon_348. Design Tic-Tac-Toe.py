#348. Design Tic-Tac-Toe
#Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

#A move is guaranteed to be valid and is placed on an empty block.
#Once a winning condition is reached, no more moves are allowed.
#A player who succeeds in placing n of their marks in a horizontal, vertical, or
#diagonal row wins the game.
#Implement the TicTacToe class:

#TicTacToe(int n) Initializes the object the size of the board n.
#int move(int row, int col, int player) Indicates that player with id player
#plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
#Follow up:
#Could you do better than O(n2) per move() operation?



class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        if n>0:
            self.length=n
            # self.board=[n*[0] for _ in range(n)]
            self.row_check={i: None for i in range(n)}
            self.col_check= {i: None for i in range(n)}
            self.top_left_bot_right=None
            self.top_right_bot_left=None


    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        ##O(1)solution
        if not self.row_check[row]: 
            self.row_check[row]=(player, 1)
        else:
            exist_player, exist_steps= self.row_check[row]
            if exist_player==player and exist_steps+1==self.length:
                return player
            elif exist_player==player:
                self.row_check[row]=(player, exist_steps+1)
        
        if not self.col_check[col]: 
            self.col_check[col]=(player, 1)
        else:
            exist_player, exist_steps= self.col_check[col]
            if exist_player==player and exist_steps+1==self.length:
                return player
            elif exist_player==player:
                self.col_check[col]=(player, exist_steps+1)
                
        if row==col:
            if not self.top_left_bot_right:
                self.top_left_bot_right=(player, 1)
            else:
                exist_player, exist_steps= self.top_left_bot_right
                if exist_player==player and exist_steps+1==self.length:
                    return player
                elif exist_player==player:
                    self.top_left_bot_right=(player, exist_steps+1)    
                    
        if row==self.length-col-1:
            if not self.top_right_bot_left:
                self.top_right_bot_left=(player, 1)
            else:
                exist_player, exist_steps= self.top_right_bot_left
                if exist_player==player and exist_steps+1==self.length:
                    return player
                elif exist_player==player:
                    self.top_right_bot_left=(player, exist_steps+1)  
                    
        return 0
    
    ##O(n solution)     
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = self.diag2 = 0
        

    def move(self, row: int, col: int, player: int) -> int:        
        new = 1 if player == 1 else -1
        self.rows[row] += new
        self.cols[col] += new
        self.diag1 += new if row == col else 0
        self.diag2 += new if row + col == self.n-1 else 0
        check = [self.rows[row], self.cols[col], self.diag1, self.diag2]
        if self.n in check or -self.n in check:
            return player
        return 0
        

        
#         ##brute force  time over limit
#         self.board[row][col]=player
#         for r in self.board:
#             if len(set(r))==1 and r[0]!=0:
#                 return r[0]
        
#         for c in range(len(self.board[0])):
#             check_col=set()
#             for r in range(len(self.board)):
#                 check_col.add(self.board[r][c])
#             if len(check_col)==1 and self.board[r][c]!=0:
#                 return self.board[r][c]
        
#         if len(set([self.board[d][d] for d in range(len(self.board))]))==1 and self.board[0][0]!=0:
#             return self.board[0][0]
        
#         if len(set([self.board[d][len(self.board)-d-1] for d in range(len(self.board))]))==1 and self.board[0][-1]!=0:
#             return self.board[0][-1]

#         return 0
                
                
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)