class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        for w in words:
            result += all(c in allowed for c in w)
        return result
