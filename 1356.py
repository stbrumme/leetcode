class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return [ b % 100_000 for b in sorted([ 100_000 * a.bit_count() + a for a in arr ])]
