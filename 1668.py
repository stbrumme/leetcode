class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while sequence.find(k * word) >= 0:
            k += 1
        return k - 1
