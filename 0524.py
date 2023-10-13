class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x : len(x), reverse = True) # longest words first

        # count letters
        fingerprint = defaultdict(int)
        for c in s:
            fingerprint[c] += 1

        result = ""
        for w in dictionary:
            # longest one found
            if len(result) > len(w):
                break

            # count letters
            freq = defaultdict(int)
            for c in w:
                freq[c] += 1

            # need to have enough matching letters
            if not all(f in fingerprint and freq[f] <= fingerprint[f] for f in freq):
                continue

            # now check their order
            pos = 0
            for c in s:
                if c != w[pos]:
                    continue

                pos += 1
                # fully matched
                if pos == len(w):
                    if not result or result > w:
                        result = w
                    break

        return result
