class RandomizedSet:
    def __init__(self):
        self.all = set() # assume hash set

    def insert(self, val: int) -> bool:
        if val not in self.all:
            self.all.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.all:
            self.all.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(tuple(self.all))
