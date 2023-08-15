class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = []
        for i in timePoints:
            parts = i.split(":")
            minutes = int(parts[0]) * 60 + int(parts[1])
            n.append(minutes)
            if (minutes < 12*60):
                n.append(minutes + 24*60)

        n.sort()

        result = n[1] - n[0]
        for i in range(1, len(n)):
            result = min(result, n[i] - n[i -1])

        return result
