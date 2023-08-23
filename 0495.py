class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last   = timeSeries[0]
        result = 0
        for start in timeSeries:
            result += min(start - last, duration)
            last = start

        return result + duration
