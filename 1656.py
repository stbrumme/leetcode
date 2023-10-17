class OrderedStream:
    def __init__(self, n: int):
        self.next = 1
        self.data = [] # min-heap

    def insert(self, idKey: int, value: str) -> List[str]:
        heappush(self.data, (idKey, value))

        while self.data and self.data[0][0] == self.next:
            self.next += 1
            yield heappop(self.data)[1]
