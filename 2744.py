class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        words = set(words) # faster lookup
        result = 0
        for w in words:
            other = w[::-1]
            if other > w and other in words:
                result += 1
        return result
