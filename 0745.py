class WordFilter:
    def __init__(self, words: List[str]):
        self.presuf = {}

        for i, w in enumerate(words):
            # all prefixes
            for left in range(1, len(w) + 1):
                prefix = w[:left]
                if prefix not in self.presuf:
                    self.presuf[prefix] = {}

                # all suffixes
                for right in range(len(w)):
                    suffix = w[right:]
                    self.presuf[prefix][suffix] = i

    def f(self, pref: str, suff: str) -> int:
        if pref not in self.presuf:
            return -1
        if suff not in self.presuf[pref]:
            return -1

        return self.presuf[pref][suff]
