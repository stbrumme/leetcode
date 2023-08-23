class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        previous = ""
        result = ""
        while freq:
            best  = ""
            count = 0
            for k in freq:
                if k != previous and freq[k] > count:
                    best = k
                    count = freq[k]

            if best == "":
                return ""

            result += best
            freq[best] -= 1
            if freq[best] == 0:
                del freq[best]

            previous = best

        return result
