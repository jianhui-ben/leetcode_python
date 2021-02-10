#904. Fruit Into Baskets

#In a row of trees, the i-th tree produces fruit with type tree[i].

#You start at any tree of your choice, then repeatedly perform the following steps:

#Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
#Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
#Note that you do not have any choice after the initial choice of starting tree: 
#    you must perform step 1, then step 2, then back to step 1, then step 2, 
#    and so on until you stop.

#You have two baskets, and each basket can carry any quantity of fruit, but 
#you want each basket to only carry one type of fruit each.

#What is the total amount of fruit you can collect with this procedure?

 

#Example 1:

#Input: [1,2,1]
#Output: 3
#Explanation: We can collect [1,2,1].



class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        ##brute force
        ans=[]
        baskets={}
        previous_type, consecutive_len= None, 1
        for i in tree:
            if i in baskets: ##existing type
                baskets[i]+=1
            elif len(baskets)<2: ## new type
                baskets[i]=1
            
            else: ##new types and the baskets have been full
                ans.append(sum(baskets.values()))
                removed_type= [fruit for fruit in baskets.keys() if fruit!=previous_type][0]
                baskets.pop(removed_type)
                baskets[previous_type]= consecutive_len
                baskets[i]=1
            if i==previous_type:
                consecutive_len+=1
            else:
                consecutive_len=1                
            previous_type=i
        ans.append(sum(baskets.values()))
        # print(ans)
        return max(ans)
            
            
                    