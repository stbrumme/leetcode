class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # idea: try to ensure s[i] < s[i+1]
        #       unless s[i] is the rightmost location of its letter
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        result = ""
        for c in s:
            freq[c] -= 1
            if c in result:
                continue

            # remove last if lexicographically bigger
            while len(result) > 0 and c < result[-1]:
                # but not if the last of its kind
                if freq[result[-1]] == 0:
                    break
                result = result[:-1]

            result += c

        return result
