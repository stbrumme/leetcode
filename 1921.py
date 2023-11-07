class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)

        # minutes left until a monster reaches the city
        duration = [ ceil(dist[i] / speed[i]) for i in range(n) ]
        for i, d in enumerate(sorted(duration)):
            if i >= d:
                return i

        # city defended
        return n
