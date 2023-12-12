class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        drive = 0
        for i in range(min(start, destination), max(start, destination)):
            drive += distance[i]
        return min(drive, total - drive)
