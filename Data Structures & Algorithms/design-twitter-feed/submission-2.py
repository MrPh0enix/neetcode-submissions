class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        tweets = self.tweetMap[userId].copy()

        for i in self.follows[userId]:
            tweets += self.tweetMap[i]

        for tweet in tweets:
            heapq.heappush(out, tweet)
            if len(out) > 10:
                heapq.heappop(out)

        return [tweetId for time, tweetId in sorted(out, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
