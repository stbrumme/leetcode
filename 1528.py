class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [ None ] * len(s)
        for c, i in zip(s, indices):
            result[i] = c
        return "".join(result)
