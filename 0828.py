class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = 0

        size = len(s)

        # positions when character was seen
        seen = defaultdict(list)
        for i, c in enumerate(s):
            seen[c].append(i)

        for c in seen:
            # padding to properly process begin and end
            have = [ -1 ] + seen[c] + [ size ]
            for prev, current, next in zip(have, have[1:], have[2:]):
                left  = current - prev
                right = next - current
                result += left * right

        return result
