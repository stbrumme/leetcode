class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev = 0
        longest = defaultdict(int)
        for r, k in zip(releaseTimes, keysPressed):
            duration   = r - prev
            longest[k] = max(longest[k], duration)
            prev = r

        result = ""
        for c in "abcdefghijklmnopqrstuvwxyz":
            if longest[result] <= longest[c]:
                result = c
        return result
