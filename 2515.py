class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        matches = [ i for i, w in enumerate(words) if w == target ]
        if not matches:
            return -1

        result = len(words)
        for m in matches:
            distance = abs(startIndex - m)
            result   = min(result, distance, len(words) - distance)
        return result
