class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        startTime.sort()
        endTime  .sort()

        a = bisect_right(startTime, queryTime)
        b = bisect_left (endTime,   queryTime)
        return a - b
