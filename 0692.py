class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        all = defaultdict(int)

        for w in words:
            all[w] += 1

        invert = defaultdict(list)
        for a in all:
            invert[all[a]].append(a)

        result = []
        for i in sorted(invert, reverse = True):
            result += sorted(invert[i])

        return result[:k]
