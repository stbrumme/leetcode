class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int)
        gaps[0] = 0 # ignore left border

        for row in wall:
            pos = 0
            for r in row[:-1]: # ignore right border
                pos += r
                gaps[pos] += 1

        return len(wall) - max(gaps.values())
