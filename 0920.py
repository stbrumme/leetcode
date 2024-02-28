class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def deeper(songs, unique):
            if songs == 0 and unique == 0:
                return 1 # empty list
            if songs == 0 or  unique == 0:
                return 0 # impossible

            result = 0

            # repeat a song
            if unique > k:
                choices = unique - k
                result  = deeper(songs - 1, unique) * choices

            # play a new song
            unplayed = n - unique
            if unplayed >= 0:
                choices = unplayed + 1
                result += deeper(songs - 1, unique - 1) * choices

            return result % 1_000_000_007

        return deeper(goal, n)
