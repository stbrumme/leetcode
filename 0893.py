class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        have = set()
        for w in words:
            even = sorted(w[ ::2])
            odd  = sorted(w[1::2])
            both = "".join(even + odd)
            have.add(both)
        return len(have)
