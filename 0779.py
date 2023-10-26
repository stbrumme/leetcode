class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # zero-based
        return (k - 1).bit_count() & 1
