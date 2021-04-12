#706. Design HashMap

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store=[]
        self.keys = set()
        
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key not in self.keys:
            self.store.append([key, value])
            self.keys.add(key)
        else:
            for entry in self.store:
                if entry[0]==key:
                    entry[1]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.keys:
            return -1
        for entry in self.store:
            if entry[0]==key:
                return entry[1]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.keys:
            self.store.remove([key, self.get(key)])
            self.keys.remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)