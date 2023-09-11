class Twitter:

    def __init__(self):
        self.tweets = {}
        self.feed   = defaultdict(list)
        self.a2b    = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        seq = len(self.tweets)
        self.tweets[seq] = tweetId
        self.feed[userId].append(seq)

    def getNewsFeed(self, userId: int) -> List[int]:
        seqs = self.feed[userId].copy()
        for i in self.a2b[userId]:
            seqs += self.feed[i]

        result = []
        for s in sorted(seqs, reverse = True):
            result.append(self.tweets[s])
            if len(result) == 10:
                break

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.a2b[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.a2b[followerId].discard(followeeId)
