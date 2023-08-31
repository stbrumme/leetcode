class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        start = [i for i in range(n+1)]
        for i in range(n+1):
            r = ranges[i]
            if r > 0:
                left  = max(i - r, 0)
                right = min(i + r, n)
                for j in range(left, right):
                    start[j] = max(start[j], right)

        pos = 0
        taps = 0
        while pos != start[pos]:
            pos = start[pos]
            taps += 1

        if pos < n:
            return -1
        else:
            return taps
