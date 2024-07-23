class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        freqA = [ 0 ] * 26
        for c in a:
            freqA[ord(c) - 97] += 1 # ord("a") == 97
        freqB = [ 0 ] * 26
        for c in b:
            freqB[ord(c) - 97] += 1

        # condition 1: need to fix the large numbers in "one" and small numbers in "two"
        # condition 2: same as condition 1 with swapped parameters
        def less(one, two):
            best = +inf
            for threshold in range(1, 26):
                low  = sum(one[ : threshold])
                high = sum(two[threshold : ])
                best = min(best, low + high)
            return best

        result = min(less(freqA, freqB), less(freqB, freqA))

        # condition 3: a = "x" * sizeA and b = "x" * sizeB
        #              where "x" is any letter (but the same for a and b)
        need = len(a) + len(b)
        for one, two in zip(freqA, freqB):
            have   = one + two
            result = min(result, need - have)

        return result
