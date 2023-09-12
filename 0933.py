class RecentCounter:
    def __init__(self):
        self.history = []

    def ping(self, t: int) -> int:
        self.history.append(t)

        while self.history[0] < t  - 3000:
            del self.history[0]

        return len(self.history)
