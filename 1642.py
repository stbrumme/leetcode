class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # idea: use bricks  if heights differ a little,
        #       use ladders if heights differ a lot

        # min-heap of buildings with small height difference
        small = []
        for i in range(1, len(heights)):
            climb = heights[i] - heights[i - 1]
            # no need for bricks or ladders
            if climb <= 0:
                continue

            # add height gap to min-heap
            heappush(small, climb)

            # climb at least one building using bricks, pick the lowest height difference
            if len(small) > ladders:
                if bricks < small[0]: # impossible to reach that building
                    return i - 1

                bricks -= heappop(small)

        return len(heights) - 1
