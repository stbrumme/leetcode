class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low  = 0
        high = len(s)
        for c in s:
            if c == "I":
                yield low
                low  += 1
            else:
                yield high
                high -= 1
        yield low
