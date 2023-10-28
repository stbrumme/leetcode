class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)
        for t in text:
            freq[t] += 1

        result = min(freq["b"], freq["a"])
        result = min(result, freq["n"])
        result = min(result, freq["l"] // 2)
        result = min(result, freq["o"] // 2)
        return result
