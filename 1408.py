class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        for v in words:
            for w in words:
                if w != v and w.find(v) != -1:
                    yield v
                    break # one match is enough
