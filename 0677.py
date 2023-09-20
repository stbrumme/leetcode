class MapSum:
    def __init__(self):
        self.data = {}

    def insert(self, key: str, val: int) -> None:
        self.data[key] = val

    def sum(self, prefix: str) -> int:
        result = 0

        k = sorted(self.data.keys())
        pos = bisect_left(k, prefix)
        while pos < len(k) and k[pos].startswith(prefix):
            result += self.data[k[pos]]
            pos += 1
        return result
