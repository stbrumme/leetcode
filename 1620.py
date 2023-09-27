class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # max. area
        x1 = x2 = towers[0][0]
        y1 = y2 = towers[0][0]
        for x, y, q in towers:
            x1 = min(x1, x)
            x2 = max(x2, x)
            y1 = min(y1, y)
            y2 = max(y2, y)

        radius2 = radius * radius

        strength = 0
        location = [ 0, 0 ]
        for x in range(x1, x2+1): # order of loops ensures lexicographical order
            for y in range(y1, y2+1):
                total = 0
                for tx, ty, q in towers:
                    # too far ?
                    dx = abs(x - tx)
                    dy = abs(y - ty)
                    dist2 = dx*dx + dy*dy
                    if dist2 > radius2: # faster if both sides are squared
                        continue

                    signal = q / (1 + sqrt(dist2))
                    total += int(signal) # round down, only seen in the example

                if strength < total:
                    strength = total
                    location = [ x, y ]

        return location
