class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for c in stones if c in jewels)
