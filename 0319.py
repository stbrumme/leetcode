class Solution:
    def bulbSwitch(self, n: int) -> int:
        # brute-force shows that bulbs at position n^2 are on, else off
        return int(n**0.5)
