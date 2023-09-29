class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.abc  = combinations(list(characters), combinationLength) # generator
        self.size = math.comb(len(characters), combinationLength)

    def next(self) -> str:
        self.size -= 1
        return "".join(next(self.abc))

    def hasNext(self) -> bool:
        return self.size > 0
