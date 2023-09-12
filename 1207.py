class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        return len(freq.values()) == len(set(freq.values()))
