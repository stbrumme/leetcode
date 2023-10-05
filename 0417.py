class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width  = len(heights[0])
        height = len(heights)


        # go upward (or at least keep the height level)
        def up(x, y, ocean):
            if (y, x) in ocean:
                return
            ocean.add((y, x))

            # something like a two-pass flood fill
            level = heights[y][x]
            if x > 0          and heights[y][x - 1] >= level:
                up(x - 1, y, ocean)
            if x < width - 1  and heights[y][x + 1] >= level:
                up(x + 1, y, ocean)
            if y > 0          and heights[y - 1][x] >= level:
                up(x, y - 1, ocean)
            if y < height - 1 and heights[y + 1][x] >= level:
                up(x, y + 1, ocean)

        pacific  = set()
        atlantic = set()

        for i in range(width):
            up(i, 0,          pacific)
            up(i, height - 1, atlantic)

        for i in range(height):
            up(0,         i,  pacific)
            up(width - 1, i,  atlantic)

        return pacific & atlantic
