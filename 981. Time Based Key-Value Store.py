#981. Time Based Key-Value Store
#Create a timebased key-value store class TimeMap, that supports two operations.

#1. set(string key, string value, int timestamp)

#Stores the key and value, along with the given timestamp.
#2. get(string key, int timestamp)

#Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
#If there are multiple such values, it returns the one with the largest timestamp_prev.
#If there are no values, it returns the empty string ("").
 

#Example 1:

#Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
#Output: [null,null,"bar","bar",null,"bar2","bar2"]
#Explanation:   
#TimeMap kv;   
#kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
#kv.get("foo", 1);  // output "bar"   
#kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
#kv.set("foo", "bar2", 4);   
#kv.get("foo", 4); // output "bar2"   
#kv.get("foo", 5); //output "bar2"   


class TimeMap:
    
    
    ## hashtable with value of dict (key= timestamp, value =  value)
    ## use extra hashtable to save the key and ordered timestamps
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stored= defaultdict(dict)
        self.saved_timestamps = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stored[key][timestamp]=value
        self.saved_timestamps[key].append(timestamp)

        

    def get(self, key: str, timestamp: int) -> str:
        
        ts= self.saved_timestamps[key]
        
        def binary_search(nums, i):
            ## find the largest one <= i
            left, right =  0, len(nums)-1
            while left<=right:
                mid = left+(right-left)//2
                if nums[mid]>i:
                    right=mid-1
                else:
                    left=mid+1
            if right<0 or nums[right]>i:
                return -1
            return nums[right]
        i = binary_search(ts, timestamp)
        if i<0: return ""
        return self.stored[key][i]
        
        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)