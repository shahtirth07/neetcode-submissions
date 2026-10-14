class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []
        users = set(self.following.get(userId, set()))
        users.add(userId)

        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(heap,(-time, tweetId, user, index))
        
        while heap and len(result) < 10:
            nagTime, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)
            if index > 0:
                index -= 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(heap, (-time, tweetId, user, index))
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

        
