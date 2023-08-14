class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        freqA = defaultdict(int)
        freqB = defaultdict(int)
        for i in range(len(A)):
            freqA[A[i]] += 1
            freqB[B[i]] += 1

            common = 0
            for j in freqA:
                common += min(freqA[j], freqB[j])

            result.append(common)

        return result
