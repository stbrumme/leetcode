class MyCalendarThree:
    def __init__(self):
        self.changes = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.changes[startTime] += 1
        self.changes[endTime]   -= 1

        result  = 0
        current = 0
        for c in sorted(self.changes):
            current += self.changes[c]
            result   = max(result, current)

        return result
