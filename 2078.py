class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        size = len(colors)
        # brute force: try all long distances first
        for distance in range(size - 1, 0, -1):
            for i in range(size - distance):
                if colors[i] != colors[i + distance]:
                    return distance
        return 0
