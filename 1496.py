class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # (x, y) offsets
        direction = { "N": (0, -1), "S": (0, +1), "W": (-1, 0), "E": (+1, 0) }

        # convert 2D to 1D for faster lookup
        norm = lambda x, y: (x * 100000) + y # abs(x) <= 10^4

        x = y = 0
        seen = set([ norm(x, y) ])
        for p in path:
            x += direction[p][0]
            y += direction[p][1]
            n  = norm(x, y)
            if n in seen:
                return True
            seen.add(n)

        return False
