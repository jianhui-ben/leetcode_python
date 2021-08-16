#465. Optimal Account Balancing
#You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

#Return the minimum number of transactions required to settle the debt.

 

#Example 1:

#Input: transactions = [[0,1,10],[2,0,5]]
#Output: 2
#Explanation:
#Person #0 gave person #1 $10.
#Person #2 gave person #0 $5.
#Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        """
        0: 5
        1: -10
        2: 5
        
        [0, 1, 2]
        choose 0 --> [1, 2]
          we have to choose 1
            --> cur_step = 1, [1: -5, 2: 5]
        time: N!, N = len(people)
        space: O(N)
        """
        balance = defaultdict(int)
        
        for transaction in transactions:
            from_, to_, val = transaction
            balance[from_] += val
            balance[to_] -= val
         
        
        balances = [val for _, val in balance.items() if val != 0]
        
        def backtrack(i, balances):
            
            if i == len(balances):
                return 0
            if balances[i] == 0:
                return backtrack(i + 1, balances)
            
            cur_balance = balances[i]
            res = float('inf')
            for next_i in range(i + 1, len(balances)):
                if balances[next_i] * cur_balance >= 0:
                    continue
                    
                balances[next_i] += cur_balance
                res = min(res, 1 + backtrack(i + 1, balances))
                balances[next_i] -= cur_balance
                
                if balances[next_i] + cur_balance == 0:
                    break
            
            return res
        