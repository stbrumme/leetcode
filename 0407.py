class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        result = 0

        height = len(heightMap)
        width  = len(heightMap[0])

        walls  = []    # min-heap
        inside = set() # cells where water might be trapped
        for y in range(height):
            for x in range(width):
                if 0 < x < width - 1 and 0 < y < height - 1:
                    inside.add(( x, y ))
                else:
                    heappush(walls, ( heightMap[y][x], x, y ))

        delta = [ 0, +1, 0, -1, 0 ] # compact representation of (0,+1), (+1,0), (0,-1), (-1, 0)
        while walls:
            # pick lowest wall, water will overflow here first
            height, x, y = heappop(walls)

            # check its four neighbors
            for dx, dy in zip(delta, delta[1 :]):
                nx = x + dx
                ny = y + dy
                if ( nx, ny ) not in inside:
                    continue

                # there could be water
                trapped = height - heightMap[ny][nx]
                if trapped > 0:
                    result += trapped

                # move wall
                heappush(walls, ( max(height, heightMap[ny][nx]), nx, ny ))
                inside.discard(( nx, ny ))

        return result
