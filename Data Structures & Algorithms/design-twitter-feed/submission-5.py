from collections import defaultdict
from typing import List
import heapq
class Twitter:

    def __init__(self):
        self.user_posts = defaultdict(list)
        self.user_memberships = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        tweet = (-self.time, tweetId, userId)
        self.user_posts[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.user_memberships[userId]
        followees.add(userId)

        tweet_pile = []
        for followee in followees:
            tweet_pile.extend(self.user_posts[followee])

        most_recent = heapq.heapify(tweet_pile)
        ans = []
        for _ in range(10):
            if tweet_pile:
                _,tweetId,_ = heapq.heappop(tweet_pile) 
                ans.append(tweetId)

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_memberships[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_memberships[followerId].discard(followeeId)