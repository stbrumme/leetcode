class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        result  = 0
        heaters = [ float("-inf") ] + sorted(heaters) + [ float("+inf") ]
        pos     = 1
        for h in sorted(houses):
            while h > heaters[pos]:
                pos += 1
            closest = min(heaters[pos] - h, h - heaters[pos - 1])
            result  = max(result, closest)

        return result
