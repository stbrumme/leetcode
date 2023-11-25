class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        yield first
        for e in encoded:
            first ^= e
            yield first
