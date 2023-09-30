class StreamChecker:
    def __init__(self, words: List[str]):
        self.abc  = defaultdict(set) # dict based on last letter
        for w in words:
            self.abc[w[-1]].add(w)

        self.stream = ""

    def query(self, letter: str) -> bool:
        self.stream += letter
        for w in self.abc[letter]:
            if self.stream.endswith(w):
                return True
        return False
