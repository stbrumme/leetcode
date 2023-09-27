class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        # largest circles first
        circles.sort(key = lambda c : c[2], reverse = True)

        # total area
        x1 = x2 = circles[0][0]
        y1 = y2 = circles[0][1]
        for c in circles:
            x1 = min(x1, c[0] - c[2])
            y1 = min(y1, c[1] - c[2])
            x2 = max(x2, c[0] + c[2])
            y2 = max(y2, c[1] + c[2])

        inside = 0
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                for c in circles:
                    dx = abs(x - c[0])
                    dy = abs(y - c[1])
                    # avoid sqrt by comparing against r^2
                    if (dx*dx + dy*dy) <= c[2]*c[2]:
                        inside += 1
                        break

        return inside
