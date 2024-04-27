class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # add one more single letter to a hash value
        def hash(have, ascii):
            have *= 29              # prime > 26
            have += ord(ascii) - 96 # ord("a") = 97, avoid "a" = 0
            have %= 1_000_000_007
            return have

        result = 0
        all = defaultdict(int)

        for w in words:
            front = 0 # hash of prefix
            for i, c in enumerate(w):
                front = hash(front, c)
                # does another word match the prefix
                if front not in all:
                    continue

                # need same suffix
                prefix = w[ : i + 1]
                if not w.endswith(prefix):
                    continue

                # maybe there are several matches
                result += all[front]

            all[front] += 1

        return result
