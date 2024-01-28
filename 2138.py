class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        for i in range(0, len(s), k):
            group = s[i : i + k]
            if len(group) < k:
                group += fill * (k - len(group))
            yield group
