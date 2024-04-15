class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        size = len(words)

        @cache
        def deeper(pos, first, last):
            if pos == size:
                return 0

            current = words[pos]

            # join(str, words[pos])
            one = deeper(pos + 1, first, current[-1])
            if current[0] == last:
                one -= 1

            # join(words[pos], str)
            two = deeper(pos + 1, current[0], last)
            if current[-1] == first:
                two -= 1

            return min(one, two) + len(current)

        first = words[0]
        return deeper(1, first[0], first[-1]) + len(first)
