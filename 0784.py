class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        dp = set([ "" ])
        for c in s:
            next = set()
            for i in dp:
                next.add(i + c.lower())
                next.add(i + c.upper())
            dp = next

        return dp
