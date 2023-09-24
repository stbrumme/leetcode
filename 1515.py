class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def dist(x, y):
            s = 0
            for p in positions:
                s += sqrt((p[0] - x)**2 + (p[1] - y)**2)
            return s

        x = y = 0
        for p in positions:
            x += p[0]
            y += p[1]
        x /= len(positions)
        y /= len(positions)
        # center of mass is a good approximation

        uncertainty = 10
        guesses = 100
        while uncertainty > 10**-12: # more precision than needed
            bestx = x
            besty = y
            best  = dist(bestx, besty)
            for _ in range(guesses):
                dx = x + uniform(-uncertainty, +uncertainty)
                dy = y + uniform(-uncertainty, +uncertainty)
                current = dist(dx, dy)
                if best > current:
                    best = current
                    bestx = dx
                    besty = dy

            x = bestx
            y = besty
            uncertainty *= 0.75

        return dist(x, y)