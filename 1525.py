class Solution:
    def numSplits(self, s: str) -> int:
        result = 0

        total = defaultdict(int)
        for c in s:
            total[c] += 1

        have  = set()
        for c in s:
            have.add(c)
            total[c] -= 1
            if total[c] == 0:
                del total[c]

            if len(have) >  len(total): # not needed, just makes it faster
                break
            if len(have) == len(total):
                result += 1

        return result
