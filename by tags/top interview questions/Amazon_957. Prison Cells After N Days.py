#957. Prison Cells After N Days
#There are 8 prison cells in a row, and each cell is either occupied or vacant.

#Each day, whether the cell is occupied or vacant changes according to the following rules:

#If a cell has two adjacent neighbors that are both occupied or both vacant, then 
#the cell becomes occupied.
#Otherwise, it becomes vacant.
#(Note that because the prison is a row, the first and the last cells in the row can't 
#have two adjacent neighbors.)

#We describe the current state of the prison in the following way: cells[i] == 1 if the 
#i-th cell is occupied, else cells[i] == 0.

#Given the initial state of the prison, return the state of the prison after N days (
#    and N such changes described above.)

 

#Example 1:

#Input: cells = [0,1,0,1,1,0,0,1], N = 7
#Output: [0,0,1,1,0,0,0,0]
#Explanation: 
#The following table summarizes the state of the prison on each day:
#Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
#Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
#Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
#Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
#Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
#Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
#Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
#Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

class Solution:
    ## K * min(2**K, N)) time, K * min(2**K, N)) space
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        self.stored=[]
        original_cell= "".join([str(i) for i in cells])
        
        def simulation(cells):
            new_cells=[0]*8
            for i in range(1, 7):
                if cells[i-1]+ cells[i+1]!=1:
                    new_cells[i]=1
                else:
                    new_cells[i]=0
            return new_cells

        for x in range(N):
            self.stored.append("".join([str(i) for i in cells]))
            cells= simulation(cells)
            saved_str= "".join([str(i) for i in cells])
            if saved_str in self.stored:
                i= self.stored.index(saved_str)
                cycle_len= x-i+1
                last_result= self.stored[i+((N-i)% cycle_len)]             
                break
        if N==len(self.stored):
            return cells
        out= [int(i) for i in last_result]
        return out
        
        
        
        
        
        
