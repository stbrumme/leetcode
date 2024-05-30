class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return bisect_left(range(min(time) * totalTrips + 1), totalTrips, key = lambda duration : sum(duration // t for t in time))
