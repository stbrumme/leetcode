class Solution:
    def sortSentence(self, s: str) -> str:
        words  = s.split(" ")
        result = [ "" ] * len(words)
        for w in words:
            pos = int(w[-1])
            result[pos - 1] = w[:-1]
        return " ".join(result)
