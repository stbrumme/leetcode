class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort by units per box
        boxTypes.sort(key = lambda x : -x[1])

        result = 0
        for boxes, units in boxTypes:
            take = min(boxes, truckSize)
            truckSize -= take
            result    += take * units

            if truckSize == 0:
                break

        return result
