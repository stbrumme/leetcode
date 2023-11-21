class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        count = defaultdict(int) # creator => total views
        best  = defaultdict(int) # creator => viewers of most viewed video
        video = defaultdict(str) # creator => ID of most viewed video

        for c, i, v in zip(creators, ids, views):
            count[c] += v

            # lowest ID if same viewers
            if best[c] == v:
                if not video[c]:
                    video[c] = i
                else:
                    video[c] = min(video[c], i)

            # more viewers than before
            if best[c] <  v:
                best [c] = v
                video[c] = i

        # most popular creators and their best video
        popular = max(count.values())
        for c in count:
            if count[c] == popular:
                yield [ c, video[c] ]
