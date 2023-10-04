class MyHashMap:
    MOD = 1023

    def hash(self, key):
        return key % self.MOD

    def __init__(self):
        self.data = []
        for _ in range(self.MOD):
            self.data.append( [] )

    def put(self, key: int, value: int) -> None:
        bucket = self.hash(key)
        if self.data[bucket]:
            for i, item in enumerate(self.data[bucket]):
                if item[0] == key:
                    self.data[bucket][i] = ( key, value )
                    return
        self.data[bucket].append(( key, value ))

    def get(self, key: int) -> int:
        bucket = self.hash(key)
        if self.data[bucket]:
            for i, item in enumerate(self.data[bucket]):
                if item[0] == key:
                    return item[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.hash(key)
        if self.data[bucket]:
            for i, item in enumerate(self.data[bucket]):
                if item[0] == key:
                    del self.data[bucket][i]
                    break
