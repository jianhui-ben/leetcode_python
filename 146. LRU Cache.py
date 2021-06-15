#146. LRU Cache
#Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

#Implement the LRUCache class:

#LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#int get(int key) Return the value of the key if the key exists, otherwise return -1.
#void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#The functions get and put must each run in O(1) average time complexity.

 

#Example 1:

#Input
#["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, null, -1, 3, 4]

#Explanation
#LRUCache lRUCache = new LRUCache(2);
#lRUCache.put(1, 1); // cache is {1=1}
#lRUCache.put(2, 2); // cache is {1=1, 2=2}
#lRUCache.get(1);    // return 1
#lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#lRUCache.get(2);    // returns -1 (not found)
#lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#lRUCache.get(1);    // return -1 (not found)
#lRUCache.get(3);    // return 3
#lRUCache.get(4);    // return 4


class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None ## node
        self.next = None ## node

class LRUCache:
    
    ## hashtable store nodes of a doubly linked list
    def __init__(self, capacity: int):
        self.store_key_nodes = {}
        self.cache_head = node(key = 0, value = 0)
        self.cache_tail = node(key = 0, value = 0)
        self.cache_head.next = self.cache_tail
        self.cache_tail.prev = self.cache_head
        self.capacity = capacity
        self.size = 0
    
    def remove(self, node):
        if not self.size:
            return
        node.next.prev = node.prev
        node.prev.next = node.next 
        self.store_key_nodes.pop(node.key)
        self.size -= 1
    
    def add_last(self, node):
        node.prev = self.cache_tail.prev
        self.cache_tail.prev.next = node
        node.next = self.cache_tail
        self.cache_tail.prev = node
        self.store_key_nodes[node.key] = node
        self.size += 1
    
    
    def get(self, key: int) -> int:
        if key not in self.store_key_nodes:
            return -1
        else:
            cur_node = self.store_key_nodes[key]
            self.remove(cur_node)
            self.add_last(cur_node)
            return cur_node.value

    def put(self, key: int, value: int) -> None:
        if key in self.store_key_nodes:
            cur_node = self.store_key_nodes[key]
            self.remove(cur_node)
            new_node = node(key = key, value = value)
            self.add_last(new_node)
        else:
            if self.size < self.capacity:
                new_node = node(key = key, value = value)
                self.add_last(new_node)
            else:                
                self.remove(self.cache_head.next)
                new_node = node(key = key, value = value)
                self.add_last(new_node)                 



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)