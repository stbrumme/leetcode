class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        result = 0

        # sort by bigger absolute axis
        data = []
        # result <= 26 because there are at most 26 distinct tags
        for (x, y), c in zip(points, s):
            distance = max(abs(x), abs(y))
            # reduce memory by keeping only the closest 26 entries
            if len(data) == 26 and distance > data[-1][0]:
                continue

            insort(data, ( distance, ord(c) - 97 )) # ord("a") = 97
            if len(data) > 26:
                data.pop()

        seen = [ False ] * 26
        size = 0 # side length of last valid square

        pending = 0 # points at the current distance
        for distance, tag in data:
            # grow the square
            if distance > size:
                size    = distance
                result += pending
                pending = 0

            # duplicated tag
            if seen[tag]:
                pending = 0
                break

            # fresh tag
            seen[tag] = True
            pending += 1

        return result + pending
