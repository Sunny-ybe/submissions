class Twitter:

    def __init__(self):
        self.time = 0

        #tweets = {userId:[]}
        self.tweets = defaultdict(list)

        #following = set(userId)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        maxHeap = []

        users = set(self.following[userId])
        users.add(userId)
        
        for followed_user in users:
            tweet_list = self.tweets[followed_user]

            if tweet_list:
                index = len(tweet_list) -1
                time, tweet_id = tweet_list[index]

                heapq.heappush(maxHeap, (-time, tweet_id, followed_user, index))

        while maxHeap and len(feed) < 10:
            negative_time, tweet_id, author, index = heapq.heappop(maxHeap)
            feed.append(tweet_id)

            prev_index = index -1

            if prev_index >= 0:
                time, prev_tweet_id = self.tweets[author][prev_index]
                heapq.heappush(maxHeap, (-time, prev_tweet_id, author, prev_index))
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
