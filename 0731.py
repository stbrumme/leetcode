class MyCalendarTwo:
    # very similar to my code for problem 732 (which I solved earlier)
    def __init__(self):
        self.changes = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.changes[start] += 1
        self.changes[end]   -= 1

        current = 0
        for c in sorted(self.changes):
            current += self.changes[c]
            if current == 3:
                # undo booking
                self.changes[start] -= 1
                self.changes[end]   += 1
                return False

        return True
