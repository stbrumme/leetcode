class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixes = defaultdict(int)
        for w in words:
            for i in range(1, len(w) + 1):
                s = w[:i]
                prefixes[s] += 1

        for w in words:
            score = 0
            for i in range(1, len(w) + 1):
                s = w[:i]
                score += prefixes[s]
            yield score
