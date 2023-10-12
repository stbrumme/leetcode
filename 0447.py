class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0

        for i in range(len(points)):
            distances = defaultdict(int)
            x1, y1 = points[i]
            for j in range(len(points)):
                if i == j:
                    continue

                x2, y2 = points[j]

                squared = (x1 - x2)**2 + (y1 - y2)**2 # no need for sqrt because a^2 == b^2 if a == b
                distances[squared] += 1

            for d in distances.values():
                result += d * (d - 1) # triangle number

        return result
