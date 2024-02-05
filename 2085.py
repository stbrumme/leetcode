class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # count words
        freq1 = defaultdict(int)
        for w in words1:
            freq1[w] += 1

        freq2 = defaultdict(int)
        for w in words2:
            if w in freq1: # this "if" makes it a tiny bit faster
                freq2[w] += 1

        # find unique words in first word list
        unique1 = set([ f for f in freq1 if freq1[f] == 1 ])
        # must be in both sets
        return sum([    1 for f in freq2 if freq2[f] == 1 and f in unique1 ])
