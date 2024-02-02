class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        last = ""
        for w in words:
            fingerprint = sorted(w)
            if last != fingerprint:
                last = fingerprint
                yield w
