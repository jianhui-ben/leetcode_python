#130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## dfs:
        ## time O(n), space O(1)
        ## no need to have mem
        def dfs(board, r, c):
            if 0<=r<=len(board)-1 and 0<=c<=len(board[0])-1 \
            and board[r][c]=='O':
                board[r][c]='E'
                dfs(board, r+1, c)
                dfs(board, r-1, c)
                dfs(board, r, c+1)
                dfs(board, r, c-1)                

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r==0 or r==len(board)-1 or c==0 or c== len(board[0])-1) \
                and board[r][c]=='O':
                    dfs(board, r, c)
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='E':
                    board[r][c]='O'
                else:
                    board[r][c]='X'
                    
        
        
