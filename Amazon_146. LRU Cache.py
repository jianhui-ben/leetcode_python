#146. LRU Cache

#Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

#Implement the LRUCache class:

#LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#int get(int key) Return the value of the key if the key exists, otherwise return -1.
#void put(int key, int value) Update the value of the key if the key exists. Otherwise,
#add the key-value pair to the cache. If the number of keys exceeds the capacity 
#from this operation, evict the least recently used key.
#Follow up:
#Could you do get and put in O(1) time complexity?



class LRUCache:

    def __init__(self, capacity: int):
        self.stored= {}
        self.mem=[]
        self.capacity= capacity
        self.size=0
        

    def get(self, key: int) -> int:
        if key in self.stored:
            self.mem.remove(key)
            self.mem.append(key)
            return self.stored[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.stored:
            self.mem.remove(key)
            self.mem.append(key)            
            self.stored[key]= value
        else:
            if self.size<self.capacity:
                self.mem.append(key) 
                self.stored[key]= value
                self.size+=1
            else:
                least_used_key=self.mem.pop(0)
                self.stored.pop(least_used_key)
                self.mem.append(key) 
                self.stored[key]= value
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)