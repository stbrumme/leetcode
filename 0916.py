class Solution:
    def freq(self, word):
        result = [0] * 26
        for i in word:
            abc = ord(i) - ord('a')
            result[abc] += 1
        return result

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2 = set(words2)

        mergedB = [0] * 26
        for b in words2:
            freqB = self.freq(b)
            for i in range(26):
                mergedB[i] = max(mergedB[i], freqB[i])

        result = []
        for a in words1:
            freqA = self.freq(a)

            ok = True
            for i in range(26):
                if mergedB[i] > freqA[i]:
                    ok = False
                    break

            if ok:
                result.append(a)

        return result
