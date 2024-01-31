class Solution:
    def maximumLength(self, s: str) -> int:
        size = len(s)
        # count all substrings
        all  = defaultdict(int)
        for i in range(size):
            for j in range(i, size):
                if s[j] != s[i]: # abort, wrong character
                    break
                all[s[i : j + 1]] += 1

        # find longest one
        result = -1
        for a in all:
            if all[a] >= 3: # but needs to occur at least thrice
                print(all[a], a)
                result = max(result, len(a))
        return result
