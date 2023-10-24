class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        unique = defaultdict(int)
        for a in answers:
            unique[a] += 1

        result = 0
        for u in unique:
            have = unique[u]
            while have > 0:
                # some rabbits of the same color plus the one you were talking to
                result += u + 1
                have   -= u + 1
                # unfortunately, multiple colors may have the same group size
                # and of course some modulo math would be faster

        return result
