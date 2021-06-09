#1348. Tweet Counts Per Frequency

#A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller time chunks based on a certain frequency (every minute, hour, or day).

#For example, the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these frequencies:

#Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
#Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
#Every day (86400-second chunks): [10,10000]
#Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (10000 in the above example).

#Design and implement an API to help the company with their analysis.

class TweetCounts:

    def __init__(self):
        self.stored = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        ## looking for the first index whose value in arr is greater than time
        def binary_search(arr, target):
            if not arr: return -1
            left, right = 0, len(arr)-1
            while left<=right:
                mid = left+(right-left)//2
                if arr[mid]<=target:
                    left=mid+1
                else:
                    right=mid-1
            if left>= len(arr) or arr[left]<=target: return -1
            return left

        i = binary_search(self.stored[tweetName], time)
        if i<0:
            self.stored[tweetName].append(time)
        else:
            self.stored[tweetName].insert(i, time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        intervals={'minute': 60, 'hour': 3600, 'day': 86400}
        interval = intervals[freq]
        out=[0]* ((endTime-startTime)//interval+1)
        
        for ts in self.stored[tweetName]:
            if 0<=(ts-startTime)//interval<=len(out)-1:
                out[(ts-startTime)//interval]+=1
                
        return out
        
        