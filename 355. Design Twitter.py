#355. Design Twitter
#Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

#Implement the Twitter class:

#Twitter() Initializes your twitter object.
#void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
#List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
#void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
#void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

class tweet():
    def __init__(self, ts, tweetId):
        self.ts = ts
        self.tweetId = tweetId
        self.next = None

import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = defaultdict(set) ## key: follower; value: followees
        ## key: user; value: list of (ts, tweetId) ascending
        self.tweets = defaultdict()
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId].add(userId)
        if userId in self.tweets:
            new_tweet = tweet(self.ts, tweetId)
            new_tweet.next = self.tweets[userId]
            self.tweets[userId] = new_tweet
        else: 
            self.tweets[userId] = tweet(self.ts, tweetId)
        self.ts += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        newsfeed, heap = [], []
        
        for users_on_newsfeed in self.users[userId]:
            if users_on_newsfeed in self.tweets:
                this_users_tweets = self.tweets[users_on_newsfeed]
                heapq.heappush(heap, (-1 * this_users_tweets.ts, this_users_tweets))
        while heap and len(newsfeed) < 10:
            cur_ts, cur_tweet = heapq.heappop(heap)
            newsfeed.append(cur_tweet.tweetId)
            if cur_tweet.next:
                next_tweet = cur_tweet.next
                heapq.heappush(heap, (-1 * next_tweet.ts, next_tweet))
        return newsfeed
        
        
        
#         ## O(nlogn), could be improve to O(n)
#         newsfeed=[]
#         for people_present_post in self.users[userId]:
#             newsfeed = newsfeed + self.tweets[people_present_post]
#         newsfeed.sort(key = lambda x: x[0], reverse =True)
#         if len(newsfeed)>10:
#             return [tweetId for ts, tweetId in newsfeed[:10]]
#         return [tweetId for ts, tweetId in newsfeed]
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.users[followerId].add(followerId)
        if followeeId not in self.users:
            self.users[followeeId].add(followeeId)
        self.users[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        else:
            return 'the person did not follow this followee before'
        
    
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


# class tweet():
#     def __init__(self, userId, tweetId):
#         self.tim = userId
#         self.tweetId = tweetId
#         self.next
        



class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = defaultdict(set) ## key: follower; value: followees
        ## key: user; value: list of (ts, tweetId) ascending
        self.tweets = defaultdict(list)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId].add(userId)
        self.tweets[userId].append((self.ts, tweetId))
        self.ts+=1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        ## O(nlogn), could be improve to O(n)
        newsfeed=[]
        for people_present_post in self.users[userId]:
            newsfeed = newsfeed + self.tweets[people_present_post]
        newsfeed.sort(key = lambda x: x[0], reverse =True)
        if len(newsfeed)>10:
            return [tweetId for ts, tweetId in newsfeed[:10]]
        return [tweetId for ts, tweetId in newsfeed]
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.users[followerId].add(followerId)
        if followeeId not in self.users:
            self.users[followeeId].add(followeeId)
        self.users[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        else:
            return 'the person did not follow this followee before'
        
    
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)