class MyHashSet:
    # simplified version of problem 706 (which I solved first)
    MOD = 1023

    def hash(self, key):
        return key % self.MOD

    def __init__(self):
        self.data = []
        for _ in range(self.MOD):
            self.data.append( [] )

    def add(self, key: int) -> None:
        bucket = self.hash(key)
        if key not in self.data[bucket]:
            self.data[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = self.hash(key)
        if self.data[bucket]:
            for i, item in enumerate(self.data[bucket]):
                if item == key:
                    del self.data[bucket][i]
                    break

    def contains(self, key: int) -> bool:
        return key in self.data[self.hash(key)]
