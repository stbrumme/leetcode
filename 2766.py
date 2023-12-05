class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        have = set(nums)
        for a, b in zip(moveFrom, moveTo):
            have.discard(a)
            have.add(b)
        return sorted(have)
