class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        cut = [ 0 ] + spaces + [ len(s) ]
        return " ".join(s[prev : pos] for prev, pos in zip(cut, cut[1 :]))
