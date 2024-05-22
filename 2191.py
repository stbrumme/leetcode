class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        result = []
        zero   = ord("0")
        for i, n in enumerate(nums):
            have = 0
            for c in str(n):
                have *= 10
                have += mapping[ord(c) - zero]
            result.append(( have, i, n ))

        return [ n for have, i, n in sorted(result) ]
