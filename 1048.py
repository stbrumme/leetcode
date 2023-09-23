class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lengths = defaultdict(set)
        for w in words:
            lengths[len(w)].add(w)

        result  = 1
        longest = max(lengths)
        todo    = { w: 1 for w in lengths[longest] }
        while longest > 1:
            next = {}
            for w in todo:
                for i in range(len(w)):
                    shorter = w[:i] + w[i+1:]
                    if shorter in lengths[len(w) - 1]:
                        if shorter in next:
                            next[shorter] = max(next[shorter], todo[w] + 1)
                        else:
                            next[shorter] = todo[w] + 1
                        result = max(result, next[shorter])

            longest -= 1
            for w in lengths[longest]:
                if w not in next:
                    next[w] = 1

            todo = next

        return result