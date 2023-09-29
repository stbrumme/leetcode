class LUPrefix:
    def __init__(self, n: int):
        self.status = [ False ] * n
        self.done   = 0

    def upload(self, video: int) -> None:
        self.status[video - 1] = True # one-based

    def longest(self) -> int:
        while self.done < len(self.status) and self.status[self.done]:
            self.done += 1
        return self.done
