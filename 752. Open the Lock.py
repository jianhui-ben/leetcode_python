#752. Open the Lock
#You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

#The lock initially starts at '0000', a string representing the state of the 4 wheels.

#You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

#Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ##BFS
        ## time complexity: O(2* # of digits(4) * 10**4+ len(D))
        ## we need to visit every lock combo, and there're 10**4 combos in total
        ## Plus we create a set for deadends
        ## For every lock combo, we can have 8 adjacent node
        ## space complexity: O(10**4+D)
        queue = ['0000']
        visited=set()
        visited.add('0000')
        step= 0
        deadends=set(deadends)
        
        def one_move(cur, visited):
            one_move_out= []
            for i in range(4):
                a, b = cur[:i]+str((int(cur[i])+1)%10)+cur[i+1:], \
                        cur[:i]+str((int(cur[i])-1)%10)+cur[i+1:]
                if a not in visited:
                    one_move_out.append(a)
                    visited.add(a)
                if b not in visited:
                    one_move_out.append(b)
                    visited.add(b)       
            return one_move_out
                
        while queue:
            temp=[]
            for cur_status in queue:
                if cur_status in deadends:
                    continue
                if cur_status== target:
                    return step
                temp=temp+ one_move(cur_status, visited)
            queue = temp
            step+=1
            
        return -1
                
                