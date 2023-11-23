class Solution:
    def longestDupSubstring(self, s: str) -> str:
        result = ""

        size = len(s)
        # degenerated input (single characters)
        if s[:-1] == s[1:]:
            return s[1:]

        # compare long chunks
        length = 1
        step   = 128
        while step >= size:
            step //= 2

        while length < size:
            # store just hashes of chunks and have trust that no collisions occur :-)
            have = defaultdict(list)
            for j in range(size - length + 1):
                h = hash(s[j : j + length])
                have[h].append(j)

            # is there at least one pair ?
            found = False
            for h in have:
                if len(have[h]) >= 2:
                    found  = True
                    pos    = have[h][0]
                    result = s[pos : pos + length]
                    break

            # no pair found, reduce chunk length
            if not found:
                if step == 1:
                    break
                length -= step
                step  //= 2

            # prevent exceeding len(s)
            while step > 1 and length + step >= size:
                step //= 2

            # even longer chunks chunks
            length += step

        return result
