class RandomizedCollection:
    def rebuild(self):
        self.all = []
        for d in self.data:
            self.all += [ d ] * self.data[d]

    def __init__(self):
        self.data = defaultdict(int)
        self.all = []
        self.dangling = 0
        self.peeks    = 0

    def insert(self, val: int) -> bool:
        self.data[val] += 1
        self.all.append(val)
        return self.data[val] == 1

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        self.data[val] -= 1
        if self.data[val] == 0:
            del self.data[val]
        self.dangling += 1
        return True

    def getRandom(self) -> int:
        self.peeks += 1
        if self.dangling > 5 or (self.peeks > 5 and self.dangling > 0):
            self.rebuild()
            self.dangling = 0
            self.peeks    = 0

        result = choice(self.all)
        if result not in self.data:
            self.rebuild()
            result = choice(self.all)
        return result
