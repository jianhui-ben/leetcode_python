#773. Sliding Puzzle
#On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

#A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

#The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

#Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
##华容道问题
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ## typical BFS
        ## time O(6!), space O(6!)
        board = [[str(i) for i in r] for r in board]
        def from_list_to_string(board):
            return ''.join(board[0])+'_'+''.join(board[1])        
        start=from_list_to_string(board)
        queue = [start]
        step=0
        visited=set([start])

        def one_move(status, visited):
            pos= status.index('0')
            r_0, c_0 = pos//4, pos%4
            status_list= [[i for i in status[:3]],[i for i in status[4:]]]
            temp_out= []
            for m, n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r_0+m, c_0+n
                if 0<=new_r<=1 and 0<=new_c<=2:
                    status_list[new_r][new_c], status_list[r_0][c_0]=\
                    status_list[r_0][c_0], status_list[new_r][new_c]
                    new_status =from_list_to_string(status_list)
                    if new_status not in visited: 
                        temp_out.append(new_status)
                        visited.add(new_status)
                    status_list[new_r][new_c], status_list[r_0][c_0]=\
                    status_list[r_0][c_0], status_list[new_r][new_c]           
            return temp_out
            
        while queue:
            temp = []
            for status in queue:
                if status =='123_450':
                    return step
                temp+=one_move(status, visited)
            queue= temp
            step+=1
        return -1
            
                
                
            