class Solution:
    def maximumLength(self, s: str) -> int:
        # split into chunks with the same character
        chunks = defaultdict(list)

        have = 0
        same = ""
        for c in s:
            if c == same:
                have += 1
            else:
                have  = 1
            chunks[c].append(have)
            same = c

        result = -1
        for c in chunks:
            # create substrings of each chunks
            spans = defaultdict(int)
            for s in sorted(chunks[c], reverse = True)[: 3]:
                for _ in range(3): # reduce by at most three
                    spans[s] += 1
                    s        -= 1

            for s in spans:
                if s > 0 and spans[s] >= 3:
                    result = max(result, s)

        return result
