class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        todo = set([ id ]) # my own ID
        seen = set()
        # basic BFS search
        for distance in range(1, level + 1):
            next = []
            for t in todo:
                seen.add(t)
                next += friends[t]
            todo = set(next) - seen

        # enumerate videos of friends at final level
        videos = defaultdict(int)
        for t in todo:
            for v in watchedVideos[t]:
                videos[v] += 1

        # least watched videos first, then ordered by name
        return sorted([ name for name, count in videos.items() ], key = lambda x : ( videos[x], x) )
