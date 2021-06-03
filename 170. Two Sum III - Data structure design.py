#170. Two Sum III - Data structure design

#Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

#Implement the TwoSum class:

#TwoSum() Initializes the TwoSum object, with an empty array initially.
#void add(int number) Adds number to the data structure.
#boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stored=defaultdict(int)        
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.stored[number]+=1


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for v, cnt in self.stored.items():
            if value-v==v:
                if cnt>1:
                    return True
                else:
                    continue
            elif value-v in self.stored:
                return True
        return False
                
        
        
        
        

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)