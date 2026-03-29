class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followers[userId].add(userId)
        
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for follower in self.followers[userId]:
            for tweet_t,tweet_id in self.tweets[follower]:
                heapq.heappush(heap,(tweet_t*-1,tweet_id))
                # if len(heap)>10:
                #     heapq.heappop(heap)
        
        ans = []
        i=0
        while i<10 and len(heap)>0:
            tweet_t,tweet_id = heapq.heappop(heap)
            ans.append(tweet_id)
            i+=1
        return ans

        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
