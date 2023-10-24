class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def distance(x, y):
            return abs(target[0] - x) + abs(target[1] - y)

        return all(distance(g[0], g[1]) > distance(0, 0) for g in ghosts)
