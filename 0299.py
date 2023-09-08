class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sec = [ c for c in secret ] # strings are immutable => convert to lists
        gue = [ c for c in guess  ]
        size = len(sec)

        bulls = 0
        for i in range(size):
            if sec[i] == gue[i]:
                bulls += 1
                # invalidate digits
                sec[i] = "x"
                gue[i] = "o"

        freqSec = defaultdict(int)
        for c in sec:
            freqSec[c] += 1

        cows = 0
        for c in gue:
            if freqSec[c] > 0:
                freqSec[c] -= 1
                cows += 1

        return str(bulls) + "A" + str(cows) + "B"
