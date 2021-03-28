#723. Candy Crush
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ## crushing step is using two pointers in each row and column
        ## falling step is using one stack per column

        ##crushing step
        while True:
            continue_ = False
            def crush(board):
                nonlocal continue_
                ## horizontally cursh
                horizontal_board, vertical_board=[list(l)for l in board], \
                [list(l)for l in board]
                for r in range(len(board)):
                    left, right=0, 0
                    while right<len(board[0]):
                        if right+1<len(board[0]) \
                        and board[r][right+1]==board[r][right]:
                            right+=1
                        elif right- left>=2:
                            for k in range(left, right+1):
                                horizontal_board[r][k]=0
                            right+=1
                            left=right
                        else:
                            right+=1
                            left=right
                ##vertically crush
                for c in range(len(board[0])):
                    left, right=0, 0
                    while right<len(board):
                        if right+1<len(board) \
                        and board[right+1][c]==board[right][c]:
                            right+=1
                        elif right- left>=2:
                            for k in range(left, right+1):
                                vertical_board[k][c]=0
                            right+=1
                            left=right
                        else:
                            right+=1
                            left=right
                for r in range(len(board)):
                    for c in range(len(board[0])):
                        if horizontal_board[r][c]==0 or vertical_board[r][c]==0:
                            if board[r][c]!=0: continue_=True
                            board[r][c]=0
                
                            

            crush(board)
            
            ## falling step:
            
            if continue_:
                for c in range(len(board[0])):
                    stack= []
                    for r in range(len(board)):
                        if board[r][c]!=0:
                            stack.append(board[r][c])
                    for r in range(len(board)-1, -1, -1):
                        if stack:
                            board[r][c]= stack.pop()
                        else:
                            board[r][c]=0
            else:
                return board
